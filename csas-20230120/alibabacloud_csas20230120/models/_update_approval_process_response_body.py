# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateApprovalProcessResponseBody(DaraModel):
    def __init__(
        self,
        process: main_models.UpdateApprovalProcessResponseBodyProcess = None,
        request_id: str = None,
    ):
        self.process = process
        self.request_id = request_id

    def validate(self):
        if self.process:
            self.process.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process is not None:
            result['Process'] = self.process.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Process') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcess()
            self.process = temp_model.from_map(m.get('Process'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateApprovalProcessResponseBodyProcess(DaraModel):
    def __init__(
        self,
        app_uninstall_policies: main_models.UpdateApprovalProcessResponseBodyProcessAppUninstallPolicies = None,
        approval_type: int = None,
        create_time: str = None,
        description: str = None,
        device_registration_policies: main_models.UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies = None,
        dlp_send_policies: main_models.UpdateApprovalProcessResponseBodyProcessDlpSendPolicies = None,
        domain_blacklist_policies: main_models.UpdateApprovalProcessResponseBodyProcessDomainBlacklistPolicies = None,
        domain_whitelist_policies: main_models.UpdateApprovalProcessResponseBodyProcessDomainWhitelistPolicies = None,
        endpoint_hardening_policies: main_models.UpdateApprovalProcessResponseBodyProcessEndpointHardeningPolicies = None,
        event_label: str = None,
        external_config: str = None,
        periphera_block_policies: main_models.UpdateApprovalProcessResponseBodyProcessPeripheraBlockPolicies = None,
        process_id: str = None,
        process_name: str = None,
        process_nodes: List[List[main_models.UpdateApprovalProcessResponseBodyProcessProcessNodes]] = None,
        software_block_policies: main_models.UpdateApprovalProcessResponseBodyProcessSoftwareBlockPolicies = None,
        software_hardening_policies: main_models.UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies = None,
    ):
        self.app_uninstall_policies = app_uninstall_policies
        self.approval_type = approval_type
        self.create_time = create_time
        self.description = description
        self.device_registration_policies = device_registration_policies
        self.dlp_send_policies = dlp_send_policies
        self.domain_blacklist_policies = domain_blacklist_policies
        self.domain_whitelist_policies = domain_whitelist_policies
        self.endpoint_hardening_policies = endpoint_hardening_policies
        self.event_label = event_label
        self.external_config = external_config
        self.periphera_block_policies = periphera_block_policies
        self.process_id = process_id
        self.process_name = process_name
        self.process_nodes = process_nodes
        self.software_block_policies = software_block_policies
        self.software_hardening_policies = software_hardening_policies

    def validate(self):
        if self.app_uninstall_policies:
            self.app_uninstall_policies.validate()
        if self.device_registration_policies:
            self.device_registration_policies.validate()
        if self.dlp_send_policies:
            self.dlp_send_policies.validate()
        if self.domain_blacklist_policies:
            self.domain_blacklist_policies.validate()
        if self.domain_whitelist_policies:
            self.domain_whitelist_policies.validate()
        if self.endpoint_hardening_policies:
            self.endpoint_hardening_policies.validate()
        if self.periphera_block_policies:
            self.periphera_block_policies.validate()
        if self.process_nodes:
            for v1 in self.process_nodes:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.software_block_policies:
            self.software_block_policies.validate()
        if self.software_hardening_policies:
            self.software_hardening_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uninstall_policies is not None:
            result['AppUninstallPolicies'] = self.app_uninstall_policies.to_map()

        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.device_registration_policies is not None:
            result['DeviceRegistrationPolicies'] = self.device_registration_policies.to_map()

        if self.dlp_send_policies is not None:
            result['DlpSendPolicies'] = self.dlp_send_policies.to_map()

        if self.domain_blacklist_policies is not None:
            result['DomainBlacklistPolicies'] = self.domain_blacklist_policies.to_map()

        if self.domain_whitelist_policies is not None:
            result['DomainWhitelistPolicies'] = self.domain_whitelist_policies.to_map()

        if self.endpoint_hardening_policies is not None:
            result['EndpointHardeningPolicies'] = self.endpoint_hardening_policies.to_map()

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.external_config is not None:
            result['ExternalConfig'] = self.external_config

        if self.periphera_block_policies is not None:
            result['PeripheraBlockPolicies'] = self.periphera_block_policies.to_map()

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        result['ProcessNodes'] = []
        if self.process_nodes is not None:
            for k1 in self.process_nodes:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ProcessNodes'].append(l1)

        if self.software_block_policies is not None:
            result['SoftwareBlockPolicies'] = self.software_block_policies.to_map()

        if self.software_hardening_policies is not None:
            result['SoftwareHardeningPolicies'] = self.software_hardening_policies.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUninstallPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessAppUninstallPolicies()
            self.app_uninstall_policies = temp_model.from_map(m.get('AppUninstallPolicies'))

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceRegistrationPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies()
            self.device_registration_policies = temp_model.from_map(m.get('DeviceRegistrationPolicies'))

        if m.get('DlpSendPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDlpSendPolicies()
            self.dlp_send_policies = temp_model.from_map(m.get('DlpSendPolicies'))

        if m.get('DomainBlacklistPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDomainBlacklistPolicies()
            self.domain_blacklist_policies = temp_model.from_map(m.get('DomainBlacklistPolicies'))

        if m.get('DomainWhitelistPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDomainWhitelistPolicies()
            self.domain_whitelist_policies = temp_model.from_map(m.get('DomainWhitelistPolicies'))

        if m.get('EndpointHardeningPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessEndpointHardeningPolicies()
            self.endpoint_hardening_policies = temp_model.from_map(m.get('EndpointHardeningPolicies'))

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('ExternalConfig') is not None:
            self.external_config = m.get('ExternalConfig')

        if m.get('PeripheraBlockPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessPeripheraBlockPolicies()
            self.periphera_block_policies = temp_model.from_map(m.get('PeripheraBlockPolicies'))

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        self.process_nodes = []
        if m.get('ProcessNodes') is not None:
            for k1 in m.get('ProcessNodes'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.UpdateApprovalProcessResponseBodyProcessProcessNodes()
                    l1.append(temp_model.from_map(k2))
                self.process_nodes.append(l1)

        if m.get('SoftwareBlockPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessSoftwareBlockPolicies()
            self.software_block_policies = temp_model.from_map(m.get('SoftwareBlockPolicies'))

        if m.get('SoftwareHardeningPolicies') is not None:
            temp_model = main_models.UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies()
            self.software_hardening_policies = temp_model.from_map(m.get('SoftwareHardeningPolicies'))

        return self

class UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessSoftwareHardeningPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessSoftwareBlockPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessSoftwareBlockPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessSoftwareBlockPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessSoftwareBlockPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessProcessNodes(DaraModel):
    def __init__(
        self,
        sase_user_id: str = None,
        username: str = None,
    ):
        self.sase_user_id = sase_user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class UpdateApprovalProcessResponseBodyProcessPeripheraBlockPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessPeripheraBlockPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessPeripheraBlockPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessPeripheraBlockPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessEndpointHardeningPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessEndpointHardeningPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessEndpointHardeningPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessEndpointHardeningPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessDomainWhitelistPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessDomainWhitelistPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDomainWhitelistPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessDomainWhitelistPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessDomainBlacklistPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessDomainBlacklistPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDomainBlacklistPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessDomainBlacklistPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessDlpSendPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessDlpSendPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDlpSendPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessDlpSendPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessDeviceRegistrationPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

class UpdateApprovalProcessResponseBodyProcessAppUninstallPolicies(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessResponseBodyProcessAppUninstallPoliciesFieldMap] = None,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        if self.field_map:
            for v1 in self.field_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_process_id is not None:
            result['ExternalProcessId'] = self.external_process_id

        result['FieldMap'] = []
        if self.field_map is not None:
            for k1 in self.field_map:
                result['FieldMap'].append(k1.to_map() if k1 else None)

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalProcessId') is not None:
            self.external_process_id = m.get('ExternalProcessId')

        self.field_map = []
        if m.get('FieldMap') is not None:
            for k1 in m.get('FieldMap'):
                temp_model = main_models.UpdateApprovalProcessResponseBodyProcessAppUninstallPoliciesFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessResponseBodyProcessAppUninstallPoliciesFieldMap(DaraModel):
    def __init__(
        self,
        display_field: str = None,
        display_field_value: str = None,
        system_field: str = None,
    ):
        self.display_field = display_field
        self.display_field_value = display_field_value
        self.system_field = system_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_field is not None:
            result['DisplayField'] = self.display_field

        if self.display_field_value is not None:
            result['DisplayFieldValue'] = self.display_field_value

        if self.system_field is not None:
            result['SystemField'] = self.system_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayField') is not None:
            self.display_field = m.get('DisplayField')

        if m.get('DisplayFieldValue') is not None:
            self.display_field_value = m.get('DisplayFieldValue')

        if m.get('SystemField') is not None:
            self.system_field = m.get('SystemField')

        return self

