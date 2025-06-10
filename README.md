# Glossary

1. [Introduction](#1-introduction)
2. [Orientations](#2-orientations)
3. [Code Only](#3-code-only)
4. [About Me](#4-about-me)
5. [Original Version](https://github.com/Samu3lb0az/WriupVolatility.git)

---

## **1. Introduction**

**Objective**: This writeup was developed to assist in **understanding the tasks** of the lab **Volatility**, providing a practical execution guide directly on the TryHackMe virtual machine. The environment already includes all pre-installed requirements (Python 3, **Volatility** tools, and necessary files), allowing you to focus on forensic analysis without worrying about setup.

**Tool**: Volatility 3.

## 2. Orientations

The orientations take place in task 10 of the Volatility module on the TryHackMe platform.

It’s important to note that all activities in task 10 are performed on TryHackMe’s own machine, which can be powered on in task 3.

---

**Prompt: What is the build version of the host machine in Case 001?**

This challenge can be solved using what was covered in previous tasks. I used the **info** plugin, which comes right after indicating the operating system in memory. In this case, we’ll use **windows.info**:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.info
```

A tip I got from a friend is that TryHackMe itself already tells you how many characters and whether there will be a special character, making it easier to search for the correct answer. With that small tip, I was able to find several answers just by analyzing what the plugin returned.

---

**Prompt: At what moment was the memory file acquired in Case 001?**

In this challenge, I used the same plugin as before. In short, I found the answer based on the module’s own teachings and by analyzing what is shown after running the plugin:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.info
```

---

**Prompt: What process can be considered suspicious in Case 001?**

**Note:** Certain special characters may not be visible on the provided VM. When copying and pasting, they will still be included.

In this challenge, we start using another plugin, **pslist**, which is also simple and requires interpretation to identify what’s asked. This TryHackMe note about special characters refers to copying and pasting from the VM into the answer field. So, write out the process name in full:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist
```

---

**Prompt: What is the parent process of the suspicious process in Case 001?**

Same plugin and interpretation:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist
```

---

**Prompt: What is the PID of the suspicious process in Case 001?**

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist
```

---

**Prompt: What is the parent process PID in Case 001?**

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist
```

---

**Prompt: What user-agent was employed by the adversary in Case 001?**

This was more challenging. We use two steps: dump the suspicious process memory (PID 1640) with **memmap** and **--dump**, then extract the user-agent:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.memmap --pid 1640 --dump
strings *.dmp | grep -i "user-agent"
```

---

**Prompt: Was Chase Bank one of the suspicious bank domains found in Case 001? (Y/N)**

Based on the previous dump, the answer is **Y**.

---

## 3. Code Only

Isolated for easy copy:

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.info
```

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist
```

```bash
vol -f /Scenarios/Investigations/Investigation-1.vmem windows.memmap --pid 1640 --dump
strings *.dmp | grep -i "user-agent"
```

```bash
vol -f /Scenarios/Investigations/Investigation-2.raw windows.pslist
```

```bash
vol -f /Scenarios/Investigations/Investigation-2.raw windows.dlllist | grep 740
```

```bash
vol -f /Scenarios/Investigations/Investigation-2.raw windows.handles | grep 1940
```

*I strongly recommend reviewing the [Orientations](#2-orientations) section to avoid conflicts or misunderstandings.*

---

## 4. About Me

*Summary information about the author.*
