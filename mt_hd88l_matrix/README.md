
# MT-VIKI MT-HD88L Matrix Switch for Home Assistant

This custom integration allows Home Assistant to control the **MT-VIKI MT-HD88L 8x8 HDMI Matrix Switch**.

It automatically creates 64 button entities (one for each Input→Output path) and sends simple HTTP commands directly to the device.

---

## 🔧 Features

- ✅ 8x8 matrix: 64 buttons
- ✅ UI-based configuration (no YAML)
- ✅ Fixed IP setup with unique-device enforcement
- ✅ Per-device HTTP communication using POST
- ✅ Prevents duplicate setup of the same IP
- ✅ Uses `mdi:hdmi-port` icons for buttons
- ✅ Works with multiple MT-VIKI switches

---

## 📦 Installation

1. Download and extract this ZIP.
2. Copy the `custom_components/mt_hd88l` folder into:
   ```
   config/custom_components/
   ```
3. Restart Home Assistant.
4. Go to **Settings → Devices & Services → Add Integration**.
5. Search for **MT-VIKI MT-HD88L Matrix Switch**.
6. Enter the **IP address** of your matrix switch (username/password/port are fixed).

---

## 🔌 Usage

After setup, you will find **64 button entities** like:

```
button.mt_hd88l_input_1_output_1
button.mt_hd88l_input_3_output_6
...
```

Each sends the command `SW <input> <output>` to the matrix via HTTP POST.

---

## 📁 GitHub Repository

🔗 https://github.com/Timman70/MT-VIKI-MT-HD88L-Matrix-Switch

---

## 🙌 Credits

Developed by **timcloud**  
Assisted by [ChatGPT from OpenAI](https://openai.com/chatgpt)

MIT License
