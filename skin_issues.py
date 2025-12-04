# skin_issues_train.py
import torch, torchvision
from torch import nn, optim
from torchvision import transforms, datasets, models

data_dir = "skin_issues_dataset"
transform = transforms.Compose([
    transforms.Resize((224,224)), transforms.ToTensor()
])
dataset = datasets.ImageFolder(data_dir, transform=transform)

train_len = int(0.8 * len(dataset))
train_ds, val_ds = torch.utils.data.random_split(dataset, [train_len, len(dataset)-train_len])
train_loader = torch.utils.data.DataLoader(train_ds, batch_size=8, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_ds, batch_size=8)

model = models.mobilenet_v2(weights='DEFAULT')
model.classifier[1] = nn.Linear(1280, len(dataset.classes))
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = model.to(device)

loss_fn = nn.BCEWithLogitsLoss()
opt = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(5):
    model.train()
    for x, y in train_loader:
        x, y = x.to(device), torch.nn.functional.one_hot(y, len(dataset.classes)).float().to(device)
        opt.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward(); opt.step()
    print(f"Epoch {epoch+1} done")

torch.save({'model': model.state_dict(), 'classes': dataset.classes}, "skin_issues_model.pth")
print("✅ Skin issues model saved!")
