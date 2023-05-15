# generated by ChatGPT on 2023-05-14 18:00

import re
import matplotlib.pyplot as plt

# Regular expression pattern to extract loss values
pattern = r"total_G: (\d+\.\d+) loss_RC: (\d+\.\d+) loss_cycle_Geom: (\d+\.\d+) loss_GAN: (\d+\.\d+) loss_D_B: (\d+\.\d+) loss_D_A: (\d+\.\d+) loss_recog: (\d+\.\d+)"

# Initialize lists to store loss values
iterations = []
total_G_losses = []
loss_RC_losses = []
loss_cycle_Geom_losses = []
loss_GAN_losses = []
loss_D_B_losses = []
loss_D_A_losses = []
loss_recog_losses = []

# Read the log file
with open('checkpoints/myexperiment_0/loss_log.txt', 'r') as f:
    lines = f.readlines()

# Extract loss values from each line
for line in lines:
    # Find lines containing loss values
    if "total_G" in line:
        matches = re.findall(pattern, line)
        if matches:
            match = matches[0]
            total_G_losses.append(float(match[0]))
            loss_RC_losses.append(float(match[1]))
            loss_cycle_Geom_losses.append(float(match[2]))
            loss_GAN_losses.append(float(match[3]))
            loss_D_B_losses.append(float(match[4]))
            loss_D_A_losses.append(float(match[5]))
            loss_recog_losses.append(float(match[6]))
            iterations.append(len(total_G_losses) * 50)  # Assuming each line represents 50 iterations

# Plot the losses
# plt.plot(iterations, total_G_losses, label='total_G')
# plt.plot(iterations, loss_RC_losses, label='loss_RC')
# plt.plot(iterations, loss_cycle_Geom_losses, label='loss_cycle_Geom')
# plt.plot(iterations, loss_GAN_losses, label='loss_GAN')
plt.plot(iterations, loss_D_B_losses, label='loss_D_B')
plt.plot(iterations, loss_D_A_losses, label='loss_D_A')
plt.plot(iterations, loss_recog_losses, label='loss_recog')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()
