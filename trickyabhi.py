o
    �sb  �                	   @   s&  d dl mZ d dlmZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
mZmZ d dlmZ e	�� Ze�d� ed d	 Zed d
 Zee�Zee�Ze�  ejZejZejZejZej Z!ej"Z#ej$Z%eeee!e#e%gZ&zd dl'Z'W n e(y�   e)e� de� �� e�*d� Y nw dd� Z+dd� Z,	 e,�  e+�  e)ed e � e)ed e � e)ed e � e)ed e � e)ed e � ee-d��Z.e.dk�reg Z/e0dd���Z1ee-de%� de� ���Z2e3e2�D ]!Z4ee-de#� de� ���Z5d�6e5�7� �Z8e�9e8ge1� e/�:e8� q�e)de!� d�� e,�  e)de%� d �� e/D ].Z;ed!e;� �ee�Z<e<�=e;� e)e#� d"�� e<ed#�� e<ed$�� e<ed%�� e<�>�  �qe-d&� W d  � n	1 �sZw   Y  e1�?�  �n�e.d'k�rGg Z@g ZAe0dd(�ZB	 z
e@�:e�CeB�� W n
 eD�y�   Y nw �qteB�?�  eEe@�d k�r�e)ed) � ed*� �npe@D ]LZFeeFd  �ZGed!eG� �ee�ZHeH�I�  eH�J� �s�zeH�KeG� e)eL� d+eG� d,e� �� W �q� e�y�   e)eeeG� d- e � eA�:eF� Y �q�w �q�eEeA�d k�re)ed. � e-d/� �neAD ]ZMe@�NeM� �qe0dd0��ZOe@D ]Z.e.d  ZPe�9ePgeO� �qW d  � n	1 �s1w   Y  eO�?�  e)ed1 e � e-d/� n�e.d*k�r�g ZQe0dd(�ZR	 z
eQ�:e�CeR�� W n
 eD�yh   Y nw �qTeR�?�  d Z4e)e#� d2�� eQD ]ZSe)e� d3e4� d4eSd  � e� �� e4d7 Z4�qzee-de� d5e� ���ZTeeQeT d  �ZGeGd6 ZUejVd7k�r�e�*d8eU� �� ne�*d9eU� �� eQeT= e0dd0�ZReQD ]	ZFe�9eFeR� �q�e)de� d:e� �� e-d/� eR�?�  n*e.d;k�re)d<� e�*d=� e)d>� e-d?� e�*d@� ne.dAk�re,�  e+�  eW�  q�)B�    )�TelegramClient)�PhoneNumberBannedError)�JoinChannelRequestN)�init�Fore)�sleepz
setapi.iniZRex�input_api_id�input_api_hashz#[i] Installing module - requests...zpip install requestsc                  C   sH   dd l } g d�}|D ]}t| �t�� |� t� �� q
tdt� d�� d S )Nr   )uN   ╔════╗────╔╗─────╔═══╦╗─╔╗uN   ║╔╗╔╗║────║║─────║╔═╗║║─║║uW   ╚╝║║╠╩╦╦══╣║╔╦╗─╔╣║─║║╚═╣╚═╦╗uW   ──║║║╔╬╣╔═╣╚╝╣║─║║╚═╝║╔╗║╔╗╠╣uW   ──║║║║║║╚═╣╔╗╣╚═╝║╔═╗║╚╝║║║║║uW   ──╚╝╚╝╚╩══╩╝╚╩═╗╔╩╝─╚╩══╩╝╚╩╝u3   ─────────────╔═╝║u3   ─────────────╚══╝z$   Version: 2.0 | Author: TrickyAbhi�
)�random�print�choice�colors�n)r   �b�char� r   �$/storage/emulated/0/nt/trickyabhi.py�banner$   s
   r   c                   C   s&   t jdkrt �d� d S t �d� d S )N�nt�cls�clear)�os�name�systemr   r   r   r   �clr9   s   
r   Tz[1] Add New Accountsz[2] Filter All Banned Accountsz[3] Delete specific accountsz[4] Member Adderz[5] Exitz
Enter Your Choice: �   zvars.txt�abr
   z& [~] Enter number of accounts to add: z [~] Enter Phone Number: � z# [i] Saved all accounts in vars.txtz" [*] Logging in from new accounts
z	sessions/u>   [+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮Lz@The_Hacking_Zonez@Techno_Trickopz@TeleModsApkz"
 Press enter to goto main menu...�   �rbz4[!] There are no accounts! Please add some and retry�   z[+] z is not bannedz is banned!zCongrats! No banned accountsz!
Press enter to goto main menu...�wbz[i] All banned accounts removedz [i] Choose an account to delete
�[z] z[+] Enter a choice: z.sessionr   zdel sessions\zrm sessions/z[+] Account Deleted�   z[+] Openning Member Adderzpython xxx.pyz[+] Successfully Filtered Adminz#
 Press enter to goto main menu....zpython trickyabhi.py�   )XZtelethon.syncr   Ztelethon.errors.rpcerrorlistr   Ztelethon.tl.functions.channelsr   �pickler   ZcsvZconfigparserZcoloramar   r   �timer   ZConfigParserZconfig�readr   r	   �intZapi_id�strZapi_hashZRESETr   ZBLUEZlgZRED�rZWHITE�wZCYAN�cyZYELLOWZyeZGREENZgrr   Zrequests�ImportErrorr   r   r   r   �input�aZnew_accs�open�gZnumber_to_add�range�iZphone_number�join�splitZparsed_number�dump�appendZnumber�c�startZ
disconnect�closeZaccountsZbanned_accs�h�load�EOFError�lenZaccountZphoneZclientZconnectZis_user_authorizedZsend_code_requestZblue�m�remove�kZPhoneZaccs�fZacc�indexZsession_filer   �exitr   r   r   r   �<module>   s"   
�


�

��

����


�� 




�