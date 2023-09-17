import wandb
wandb.init(project="hippo", name = "test")
wandb.log(wandb.log({"loss": 5.2}, step = 3))