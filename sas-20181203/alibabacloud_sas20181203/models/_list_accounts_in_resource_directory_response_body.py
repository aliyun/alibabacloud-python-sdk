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
        # The members in the resource directory.
        self.accounts = accounts
        # The request ID.
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
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # This parameter is deprecated and should be ignored.
        self.buy_sas = buy_sas
        # Whether a yearly or monthly subscription of Cloud Security Center is purchased. Values:
        # - **true**: Yes
        # - **false**: No
        self.buy_sas_new = buy_sas_new
        # Subscription type. Values:
        # * **0**: Prepaid
        # * **1**: Pay-As-You-Go
        self.charge_type = charge_type
        # The name of the member.
        self.display_name = display_name
        # The ID of the folder in the resource directory.
        self.folder_id = folder_id
        # Instance purchase type. Values:
        # - **0**: Self-purchased
        # - **1**: Multi-account allocation
        self.instance_buy_type = instance_buy_type
        # Indicates whether the member is an administrator account of the resource directory. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.is_ma_account = is_ma_account
        # Indicates whether the member is marked as followed.
        self.is_marked = is_marked
        # Indicates whether the member is a delegated administrator account of Security Center. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.is_sas_da_account = is_sas_da_account
        # Indicates whether the member is an account of the threat analysis and response feature. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.is_siem_control_account = is_siem_control_account
        # Indicates whether the member is a delegated administrator account of the threat analysis and response feature. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.is_siem_da_account = is_siem_da_account
        # Post-paid module switch. Values:
        # - **0**: Off
        # - **1**: On
        self.post_basic_service = post_basic_service
        # The switch status of the pay-as-you-go module. The value is a JSON string. Valid values:
        # 
        # *   Key:
        # 
        #     *   **VUL**: vulnerability fixing module
        #     *   **CSPM**: cloud service configuration check module
        #     *   **AGENTLESS**: agentless detection module
        #     *   **SERVERLESS**: serverless asset module
        # 
        # *   Value: A value of 0 specifies disabled. A value of 1 specifies enabled.
        # 
        # >  If you do not specify a value for a module, the original value of the module is retained.
        self.post_pay_module_switch = post_pay_module_switch
        # Cloud Security Center Instance ID.
        self.sale_instance = sale_instance
        # The edition of Security Center that you use. Valid value:
        # 
        # *   **0** or **1**: Basic
        # *   **2** or **3**: Enterprise
        # *   **5**: Advanced
        # *   **6**: Anti-virus
        # *   **7**: Ultimate
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

