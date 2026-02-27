# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListAssociatedTransferSettingResponseBody(DaraModel):
    def __init__(
        self,
        associated_transfer_setting: main_models.ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting = None,
        request_id: str = None,
    ):
        # The settings of the Transfer Associated Resources feature.
        self.associated_transfer_setting = associated_transfer_setting
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.associated_transfer_setting:
            self.associated_transfer_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_transfer_setting is not None:
            result['AssociatedTransferSetting'] = self.associated_transfer_setting.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedTransferSetting') is not None:
            temp_model = main_models.ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting()
            self.associated_transfer_setting = temp_model.from_map(m.get('AssociatedTransferSetting'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAssociatedTransferSettingResponseBodyAssociatedTransferSetting(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        enable_existing_resources_transfer: str = None,
        rule_settings: List[main_models.ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings] = None,
        status: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # Indicates whether the Transfer Existing Associated Resources feature is enabled. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer
        # The settings of transfer rules.
        self.rule_settings = rule_settings
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        self.status = status

    def validate(self):
        if self.rule_settings:
            for v1 in self.rule_settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer

        result['RuleSettings'] = []
        if self.rule_settings is not None:
            for k1 in self.rule_settings:
                result['RuleSettings'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')

        self.rule_settings = []
        if m.get('RuleSettings') is not None:
            for k1 in m.get('RuleSettings'):
                temp_model = main_models.ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings()
                self.rule_settings.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListAssociatedTransferSettingResponseBodyAssociatedTransferSettingRuleSettings(DaraModel):
    def __init__(
        self,
        associated_resource_type: str = None,
        associated_service: str = None,
        master_resource_type: str = None,
        master_service: str = None,
        status: str = None,
    ):
        # The type of the associated resource.
        self.associated_resource_type = associated_resource_type
        # The service code of the associated resource.
        self.associated_service = associated_service
        # The type of the primary resource.
        self.master_resource_type = master_resource_type
        # The service code of the primary resource.
        self.master_service = master_service
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associated_resource_type is not None:
            result['AssociatedResourceType'] = self.associated_resource_type

        if self.associated_service is not None:
            result['AssociatedService'] = self.associated_service

        if self.master_resource_type is not None:
            result['MasterResourceType'] = self.master_resource_type

        if self.master_service is not None:
            result['MasterService'] = self.master_service

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociatedResourceType') is not None:
            self.associated_resource_type = m.get('AssociatedResourceType')

        if m.get('AssociatedService') is not None:
            self.associated_service = m.get('AssociatedService')

        if m.get('MasterResourceType') is not None:
            self.master_resource_type = m.get('MasterResourceType')

        if m.get('MasterService') is not None:
            self.master_service = m.get('MasterService')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

