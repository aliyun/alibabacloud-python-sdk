# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAccountsInResourceDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        accounts: List[main_models.ListAccountsInResourceDirectoryResponseBodyAccounts] = None,
        request_id: str = None,
    ):
        # La liste des comptes membres dans le répertoire de ressources.
        self.accounts = accounts
        # L\\"identifiant de la requête. Il s\\"agit d\\"un identifiant unique généré par Alibaba Cloud pour la requête. Vous pouvez l\\"utiliser pour le dépannage.
        self.request_id = request_id

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.ListAccountsInResourceDirectoryResponseBodyAccounts()
                self.accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccountsInResourceDirectoryResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        buy_sas: int = None,
        buy_sas_new: bool = None,
        charge_type: int = None,
        display_name: str = None,
        folder_id: str = None,
        instance_buy_type: int = None,
        is_ma_account: str = None,
        is_marked: str = None,
        is_sas_da_account: str = None,
        is_siem_control_account: str = None,
        is_siem_da_account: str = None,
        post_basic_service: int = None,
        post_pay_module_switch: str = None,
        sale_instance: str = None,
        sas_version: str = None,
    ):
        # L\\"identifiant de compte Alibaba Cloud du membre.
        self.account_id = account_id
        # Ce paramètre est obsolète et ne doit plus être utilisé.
        self.buy_sas = buy_sas
        # Indique si une instance Security Center en abonnement a été souscrite. Valeurs valides :
        # - **true**
        # - **false**.
        self.buy_sas_new = buy_sas_new
        # Le mode de facturation de l\\"abonnement. Valeurs valides :
        # * **0** : prépayé
        # * **1** : paiement à l\\"usage.
        self.charge_type = charge_type
        # Le nom du compte.
        self.display_name = display_name
        # L\\"identifiant du dossier dans le répertoire de ressources.
        self.folder_id = folder_id
        # Le type d\\"achat de l\\"instance. Valeurs valides :
        # - **0** : achat direct
        # - **1** : alloué via la gestion multi-comptes.
        self.instance_buy_type = instance_buy_type
        # Indique si le compte est le compte de gestion du répertoire de ressources. Valeurs valides :
        # 
        # - **yes**
        # 
        # - **no**.
        self.is_ma_account = is_ma_account
        # Indique si le compte est marqué comme suivi.
        self.is_marked = is_marked
        # Indique si le compte est un compte administrateur délégué de Security Center. Valeurs valides :
        # 
        # - **yes**
        # 
        # - **no**.
        self.is_sas_da_account = is_sas_da_account
        # Indique si le compte est un compte de gestion de Cloud Threat Detection and Response (CTDR). Valeurs valides :
        # 
        # - **yes**
        # 
        # - **no**.
        self.is_siem_control_account = is_siem_control_account
        # Indique si le compte est un compte administrateur délégué de Cloud Threat Detection and Response (CTDR). Valeurs valides :
        # 
        # - **yes**
        # 
        # - **no**.
        self.is_siem_da_account = is_siem_da_account
        # Le commutateur de module à paiement à l\\"usage. Valeurs valides :
        # - **0** : désactivé
        # - **1** : activé.
        self.post_basic_service = post_basic_service
        # L\\"état des commutateurs de modules à paiement à l\\"usage, au format JsonString. Valeurs valides :
        # - Clé :
        #   - **VUL** : module de gestion des vulnérabilités
        #   - **CSPM** : module Cloud Security Posture Management (CSPM)
        #   - **AGENTLESS** : module de détection sans agent
        #   - **SERVERLESS** : module de ressources serverless
        #   - **CTDR** : module Cloud Threat Detection and Response (CTDR)
        #   - **RASP** : module Runtime Application Self-Protection (RASP)
        #   - **SDK** : module SDK de détection de fichiers malveillants
        #   - **POST_HOST** : module de sécurité des hôtes et des conteneurs
        # - Valeur : 0 indique désactivé. 1 indique activé.
        self.post_pay_module_switch = post_pay_module_switch
        # L\\"identifiant de l\\"instance Security Center.
        self.sale_instance = sale_instance
        # L\\"édition souscrite de Security Center. Valeurs valides :
        # 
        # - **0** ou **1** : Édition gratuite
        # - **2** ou **3** : Édition Enterprise  
        # - **5** : Édition Premium  
        # - **6** : Édition Anti-virus 
        # - **7** : Édition Ultimate.
        self.sas_version = sas_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.buy_sas is not None:
            result['BuySas'] = self.buy_sas

        if self.buy_sas_new is not None:
            result['BuySasNew'] = self.buy_sas_new

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.instance_buy_type is not None:
            result['InstanceBuyType'] = self.instance_buy_type

        if self.is_ma_account is not None:
            result['IsMaAccount'] = self.is_ma_account

        if self.is_marked is not None:
            result['IsMarked'] = self.is_marked

        if self.is_sas_da_account is not None:
            result['IsSasDaAccount'] = self.is_sas_da_account

        if self.is_siem_control_account is not None:
            result['IsSiemControlAccount'] = self.is_siem_control_account

        if self.is_siem_da_account is not None:
            result['IsSiemDaAccount'] = self.is_siem_da_account

        if self.post_basic_service is not None:
            result['PostBasicService'] = self.post_basic_service

        if self.post_pay_module_switch is not None:
            result['PostPayModuleSwitch'] = self.post_pay_module_switch

        if self.sale_instance is not None:
            result['SaleInstance'] = self.sale_instance

        if self.sas_version is not None:
            result['SasVersion'] = self.sas_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BuySas') is not None:
            self.buy_sas = m.get('BuySas')

        if m.get('BuySasNew') is not None:
            self.buy_sas_new = m.get('BuySasNew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('InstanceBuyType') is not None:
            self.instance_buy_type = m.get('InstanceBuyType')

        if m.get('IsMaAccount') is not None:
            self.is_ma_account = m.get('IsMaAccount')

        if m.get('IsMarked') is not None:
            self.is_marked = m.get('IsMarked')

        if m.get('IsSasDaAccount') is not None:
            self.is_sas_da_account = m.get('IsSasDaAccount')

        if m.get('IsSiemControlAccount') is not None:
            self.is_siem_control_account = m.get('IsSiemControlAccount')

        if m.get('IsSiemDaAccount') is not None:
            self.is_siem_da_account = m.get('IsSiemDaAccount')

        if m.get('PostBasicService') is not None:
            self.post_basic_service = m.get('PostBasicService')

        if m.get('PostPayModuleSwitch') is not None:
            self.post_pay_module_switch = m.get('PostPayModuleSwitch')

        if m.get('SaleInstance') is not None:
            self.sale_instance = m.get('SaleInstance')

        if m.get('SasVersion') is not None:
            self.sas_version = m.get('SasVersion')

        return self

