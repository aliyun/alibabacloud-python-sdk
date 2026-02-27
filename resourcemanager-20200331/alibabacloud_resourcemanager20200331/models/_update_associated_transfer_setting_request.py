# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class UpdateAssociatedTransferSettingRequest(DaraModel):
    def __init__(
        self,
        enable_existing_resources_transfer: str = None,
        rule_settings: List[main_models.UpdateAssociatedTransferSettingRequestRuleSettings] = None,
    ):
        # Specifies whether to enable the Transfer Existing Associated Resources feature. Valid values:
        # 
        # *   false
        # *   true
        self.enable_existing_resources_transfer = enable_existing_resources_transfer
        # The settings of transfer rules.
        self.rule_settings = rule_settings

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
        if self.enable_existing_resources_transfer is not None:
            result['EnableExistingResourcesTransfer'] = self.enable_existing_resources_transfer

        result['RuleSettings'] = []
        if self.rule_settings is not None:
            for k1 in self.rule_settings:
                result['RuleSettings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistingResourcesTransfer') is not None:
            self.enable_existing_resources_transfer = m.get('EnableExistingResourcesTransfer')

        self.rule_settings = []
        if m.get('RuleSettings') is not None:
            for k1 in m.get('RuleSettings'):
                temp_model = main_models.UpdateAssociatedTransferSettingRequestRuleSettings()
                self.rule_settings.append(temp_model.from_map(k1))

        return self

class UpdateAssociatedTransferSettingRequestRuleSettings(DaraModel):
    def __init__(
        self,
        associated_resource_type: str = None,
        associated_service: str = None,
        master_resource_type: str = None,
        master_service: str = None,
        status: str = None,
    ):
        # The type of the associated resource.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.associated_resource_type = associated_resource_type
        # The service code of the associated resource.
        # 
        # You can obtain the service code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.associated_service = associated_service
        # The type of the primary resource.
        # 
        # You can obtain the resource type from the **Resource type** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.master_resource_type = master_resource_type
        # The service code of the primary resource.
        # 
        # You can obtain the service code from the **Service code** column in [Services that work with Resource Group](https://help.aliyun.com/document_detail/94479.html).
        self.master_service = master_service
        # The status of the Transfer Associated Resources feature. Valid values:
        # 
        # *   Enable: enabled
        # *   Disable: disabled
        # 
        # This parameter is required.
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

