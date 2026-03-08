{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f5374ec-2b78-412d-b7b9-616e7774ad39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pandas in ./Library/Python/3.9/lib/python/site-packages (2.3.3)\n",
      "Requirement already satisfied: streamlit in ./Library/Python/3.9/lib/python/site-packages (1.50.0)\n",
      "Collecting plotly\n",
      "  Downloading plotly-6.6.0-py3-none-any.whl.metadata (8.5 kB)\n",
      "Requirement already satisfied: numpy>=1.22.4 in ./Library/Python/3.9/lib/python/site-packages (from pandas) (2.0.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in ./Library/Python/3.9/lib/python/site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./Library/Python/3.9/lib/python/site-packages (from pandas) (2026.1.post1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in ./Library/Python/3.9/lib/python/site-packages (from pandas) (2025.3)\n",
      "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: blinker<2,>=1.5.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (1.9.0)\n",
      "Requirement already satisfied: cachetools<7,>=4.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (6.2.6)\n",
      "Requirement already satisfied: click<9,>=7.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (8.1.8)\n",
      "Requirement already satisfied: packaging<26,>=20 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (25.0)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (11.3.0)\n",
      "Requirement already satisfied: protobuf<7,>=3.20 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (6.33.5)\n",
      "Requirement already satisfied: pyarrow>=7.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (21.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (2.32.5)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (9.1.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (4.15.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (3.1.46)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in ./Library/Python/3.9/lib/python/site-packages (from streamlit) (6.5.4)\n",
      "Requirement already satisfied: jinja2 in ./Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
      "Requirement already satisfied: jsonschema>=3.0 in ./Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)\n",
      "Requirement already satisfied: narwhals>=1.14.2 in ./Library/Python/3.9/lib/python/site-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.17.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in ./Library/Python/3.9/lib/python/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in ./Library/Python/3.9/lib/python/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in ./Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.4.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (3.11)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in ./Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2.6.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./Library/Python/3.9/lib/python/site-packages (from requests<3,>=2.27->streamlit) (2026.1.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in ./Library/Python/3.9/lib/python/site-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in ./Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.4.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in ./Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in ./Library/Python/3.9/lib/python/site-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)\n",
      "Requirement already satisfied: six>=1.5 in /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/site-packages (from python-dateutil>=2.8.2->pandas) (1.15.0)\n",
      "Downloading plotly-6.6.0-py3-none-any.whl (9.9 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m5.0 MB/s\u001b[0m  \u001b[33m0:00:02\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hInstalling collected packages: plotly\n",
      "Successfully installed plotly-6.6.0\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas streamlit plotly\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "935b1edf-9cbf-4c51-a4ab-570b2aa7722e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-08 14:05:07.662 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.767 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/m12020/Library/Python/3.9/lib/python/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-03-08 14:05:07.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.768 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.770 Session state does not function when running a script without `streamlit run`\n",
      "2026-03-08 14:05:07.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.770 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.771 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.775 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.775 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.776 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.776 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.777 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.778 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.780 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-08 14:05:07.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Add Basic Billing Interface\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "st.title(\"Electrical Shop Billing\")\n",
    "\n",
    "product = st.text_input(\"Product Name\")\n",
    "\n",
    "qty = st.number_input(\"Quantity\", min_value=1)\n",
    "\n",
    "payment = st.selectbox(\"Payment Type\", [\"Cash\",\"Credit\"])\n",
    "\n",
    "if st.button(\"Generate Bill\"):\n",
    "\n",
    "    total = qty * 10\n",
    "\n",
    "    st.success(f\"Bill Generated: {total}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a50e055-fa15-445a-89e9-2d691fc28b86",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
