# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateApprovalProcessResponseBody(DaraModel):
    def __init__(
        self,
        process: main_models.CreateApprovalProcessResponseBodyProcess = None,
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
            temp_model = main_models.CreateApprovalProcessResponseBodyProcess()
            self.process = temp_model.from_map(m.get('Process'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateApprovalProcessResponseBodyProcess(DaraModel):
    def __init__(
        self,
        app_uninstall_policies: main_models.CreateApprovalProcessResponseBodyProcessAppUninstallPolicies = None,
        create_time: str = None,
        description: str = None,
        device_registration_policies: main_models.CreateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies = None,
        dlp_send_policies: main_models.CreateApprovalProcessResponseBodyProcessDlpSendPolicies = None,
        domain_blacklist_policies: main_models.CreateApprovalProcessResponseBodyProcessDomainBlacklistPolicies = None,
        domain_whitelist_policies: main_models.CreateApprovalProcessResponseBodyProcessDomainWhitelistPolicies = None,
        endpoint_hardening_policies: main_models.CreateApprovalProcessResponseBodyProcessEndpointHardeningPolicies = None,
        peripheral_block_policies: main_models.CreateApprovalProcessResponseBodyProcessPeripheralBlockPolicies = None,
        process_id: str = None,
        process_name: str = None,
        process_nodes: List[List[main_models.CreateApprovalProcessResponseBodyProcessProcessNodes]] = None,
        software_block_policies: main_models.CreateApprovalProcessResponseBodyProcessSoftwareBlockPolicies = None,
        software_hardening_policies: main_models.CreateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies = None,
    ):
        self.app_uninstall_policies = app_uninstall_policies
        self.create_time = create_time
        self.description = description
        self.device_registration_policies = device_registration_policies
        self.dlp_send_policies = dlp_send_policies
        self.domain_blacklist_policies = domain_blacklist_policies
        self.domain_whitelist_policies = domain_whitelist_policies
        self.endpoint_hardening_policies = endpoint_hardening_policies
        self.peripheral_block_policies = peripheral_block_policies
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
        if self.peripheral_block_policies:
            self.peripheral_block_policies.validate()
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

        if self.peripheral_block_policies is not None:
            result['PeripheralBlockPolicies'] = self.peripheral_block_policies.to_map()

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
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessAppUninstallPolicies()
            self.app_uninstall_policies = temp_model.from_map(m.get('AppUninstallPolicies'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceRegistrationPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies()
            self.device_registration_policies = temp_model.from_map(m.get('DeviceRegistrationPolicies'))

        if m.get('DlpSendPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessDlpSendPolicies()
            self.dlp_send_policies = temp_model.from_map(m.get('DlpSendPolicies'))

        if m.get('DomainBlacklistPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessDomainBlacklistPolicies()
            self.domain_blacklist_policies = temp_model.from_map(m.get('DomainBlacklistPolicies'))

        if m.get('DomainWhitelistPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessDomainWhitelistPolicies()
            self.domain_whitelist_policies = temp_model.from_map(m.get('DomainWhitelistPolicies'))

        if m.get('EndpointHardeningPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessEndpointHardeningPolicies()
            self.endpoint_hardening_policies = temp_model.from_map(m.get('EndpointHardeningPolicies'))

        if m.get('PeripheralBlockPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessPeripheralBlockPolicies()
            self.peripheral_block_policies = temp_model.from_map(m.get('PeripheralBlockPolicies'))

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        self.process_nodes = []
        if m.get('ProcessNodes') is not None:
            for k1 in m.get('ProcessNodes'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.CreateApprovalProcessResponseBodyProcessProcessNodes()
                    l1.append(temp_model.from_map(k2))
                self.process_nodes.append(l1)

        if m.get('SoftwareBlockPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessSoftwareBlockPolicies()
            self.software_block_policies = temp_model.from_map(m.get('SoftwareBlockPolicies'))

        if m.get('SoftwareHardeningPolicies') is not None:
            temp_model = main_models.CreateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies()
            self.software_hardening_policies = temp_model.from_map(m.get('SoftwareHardeningPolicies'))

        return self

class CreateApprovalProcessResponseBodyProcessSoftwareHardeningPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessSoftwareBlockPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessProcessNodes(DaraModel):
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

class CreateApprovalProcessResponseBodyProcessPeripheralBlockPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessEndpointHardeningPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessDomainWhitelistPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessDomainBlacklistPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessDlpSendPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessDeviceRegistrationPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class CreateApprovalProcessResponseBodyProcessAppUninstallPolicies(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
        schema_id: str = None,
    ):
        self.policy_ids = policy_ids
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

