# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateApprovalProcessRequest(DaraModel):
    def __init__(
        self,
        approval_type: int = None,
        description: str = None,
        event_label: str = None,
        external_config: str = None,
        match_schema_configs: main_models.UpdateApprovalProcessRequestMatchSchemaConfigs = None,
        match_schemas: main_models.UpdateApprovalProcessRequestMatchSchemas = None,
        process_id: str = None,
        process_name: str = None,
        process_nodes: List[List[str]] = None,
    ):
        self.approval_type = approval_type
        self.description = description
        self.event_label = event_label
        self.external_config = external_config
        self.match_schema_configs = match_schema_configs
        self.match_schemas = match_schemas
        # This parameter is required.
        self.process_id = process_id
        self.process_name = process_name
        self.process_nodes = process_nodes

    def validate(self):
        if self.match_schema_configs:
            self.match_schema_configs.validate()
        if self.match_schemas:
            self.match_schemas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.description is not None:
            result['Description'] = self.description

        if self.event_label is not None:
            result['EventLabel'] = self.event_label

        if self.external_config is not None:
            result['ExternalConfig'] = self.external_config

        if self.match_schema_configs is not None:
            result['MatchSchemaConfigs'] = self.match_schema_configs.to_map()

        if self.match_schemas is not None:
            result['MatchSchemas'] = self.match_schemas.to_map()

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_nodes is not None:
            result['ProcessNodes'] = self.process_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventLabel') is not None:
            self.event_label = m.get('EventLabel')

        if m.get('ExternalConfig') is not None:
            self.external_config = m.get('ExternalConfig')

        if m.get('MatchSchemaConfigs') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigs()
            self.match_schema_configs = temp_model.from_map(m.get('MatchSchemaConfigs'))

        if m.get('MatchSchemas') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemas()
            self.match_schemas = temp_model.from_map(m.get('MatchSchemas'))

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessNodes') is not None:
            self.process_nodes = m.get('ProcessNodes')

        return self

class UpdateApprovalProcessRequestMatchSchemas(DaraModel):
    def __init__(
        self,
        app_uninstall_schema_id: str = None,
        device_registration_schema_id: str = None,
        dlp_send_schema_id: str = None,
        domain_blacklist_schema_id: str = None,
        domain_whitelist_schema_id: str = None,
        endpoint_hardening_schema_id: str = None,
        peripheral_block_schema_id: str = None,
        software_block_schema_id: str = None,
        software_hardening_schema_id: str = None,
    ):
        self.app_uninstall_schema_id = app_uninstall_schema_id
        self.device_registration_schema_id = device_registration_schema_id
        self.dlp_send_schema_id = dlp_send_schema_id
        self.domain_blacklist_schema_id = domain_blacklist_schema_id
        self.domain_whitelist_schema_id = domain_whitelist_schema_id
        self.endpoint_hardening_schema_id = endpoint_hardening_schema_id
        self.peripheral_block_schema_id = peripheral_block_schema_id
        self.software_block_schema_id = software_block_schema_id
        self.software_hardening_schema_id = software_hardening_schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uninstall_schema_id is not None:
            result['AppUninstallSchemaId'] = self.app_uninstall_schema_id

        if self.device_registration_schema_id is not None:
            result['DeviceRegistrationSchemaId'] = self.device_registration_schema_id

        if self.dlp_send_schema_id is not None:
            result['DlpSendSchemaId'] = self.dlp_send_schema_id

        if self.domain_blacklist_schema_id is not None:
            result['DomainBlacklistSchemaId'] = self.domain_blacklist_schema_id

        if self.domain_whitelist_schema_id is not None:
            result['DomainWhitelistSchemaId'] = self.domain_whitelist_schema_id

        if self.endpoint_hardening_schema_id is not None:
            result['EndpointHardeningSchemaId'] = self.endpoint_hardening_schema_id

        if self.peripheral_block_schema_id is not None:
            result['PeripheralBlockSchemaId'] = self.peripheral_block_schema_id

        if self.software_block_schema_id is not None:
            result['SoftwareBlockSchemaId'] = self.software_block_schema_id

        if self.software_hardening_schema_id is not None:
            result['SoftwareHardeningSchemaId'] = self.software_hardening_schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUninstallSchemaId') is not None:
            self.app_uninstall_schema_id = m.get('AppUninstallSchemaId')

        if m.get('DeviceRegistrationSchemaId') is not None:
            self.device_registration_schema_id = m.get('DeviceRegistrationSchemaId')

        if m.get('DlpSendSchemaId') is not None:
            self.dlp_send_schema_id = m.get('DlpSendSchemaId')

        if m.get('DomainBlacklistSchemaId') is not None:
            self.domain_blacklist_schema_id = m.get('DomainBlacklistSchemaId')

        if m.get('DomainWhitelistSchemaId') is not None:
            self.domain_whitelist_schema_id = m.get('DomainWhitelistSchemaId')

        if m.get('EndpointHardeningSchemaId') is not None:
            self.endpoint_hardening_schema_id = m.get('EndpointHardeningSchemaId')

        if m.get('PeripheralBlockSchemaId') is not None:
            self.peripheral_block_schema_id = m.get('PeripheralBlockSchemaId')

        if m.get('SoftwareBlockSchemaId') is not None:
            self.software_block_schema_id = m.get('SoftwareBlockSchemaId')

        if m.get('SoftwareHardeningSchemaId') is not None:
            self.software_hardening_schema_id = m.get('SoftwareHardeningSchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigs(DaraModel):
    def __init__(
        self,
        app_uninstall_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfig = None,
        device_registration_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfig = None,
        dlp_send_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfig = None,
        domain_blacklist_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfig = None,
        domain_whitelist_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfig = None,
        endpoint_hardening_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfig = None,
        peripheral_block_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfig = None,
        software_block_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfig = None,
        software_hardening_schema_config: main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfig = None,
    ):
        self.app_uninstall_schema_config = app_uninstall_schema_config
        self.device_registration_schema_config = device_registration_schema_config
        self.dlp_send_schema_config = dlp_send_schema_config
        self.domain_blacklist_schema_config = domain_blacklist_schema_config
        self.domain_whitelist_schema_config = domain_whitelist_schema_config
        self.endpoint_hardening_schema_config = endpoint_hardening_schema_config
        self.peripheral_block_schema_config = peripheral_block_schema_config
        self.software_block_schema_config = software_block_schema_config
        self.software_hardening_schema_config = software_hardening_schema_config

    def validate(self):
        if self.app_uninstall_schema_config:
            self.app_uninstall_schema_config.validate()
        if self.device_registration_schema_config:
            self.device_registration_schema_config.validate()
        if self.dlp_send_schema_config:
            self.dlp_send_schema_config.validate()
        if self.domain_blacklist_schema_config:
            self.domain_blacklist_schema_config.validate()
        if self.domain_whitelist_schema_config:
            self.domain_whitelist_schema_config.validate()
        if self.endpoint_hardening_schema_config:
            self.endpoint_hardening_schema_config.validate()
        if self.peripheral_block_schema_config:
            self.peripheral_block_schema_config.validate()
        if self.software_block_schema_config:
            self.software_block_schema_config.validate()
        if self.software_hardening_schema_config:
            self.software_hardening_schema_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_uninstall_schema_config is not None:
            result['AppUninstallSchemaConfig'] = self.app_uninstall_schema_config.to_map()

        if self.device_registration_schema_config is not None:
            result['DeviceRegistrationSchemaConfig'] = self.device_registration_schema_config.to_map()

        if self.dlp_send_schema_config is not None:
            result['DlpSendSchemaConfig'] = self.dlp_send_schema_config.to_map()

        if self.domain_blacklist_schema_config is not None:
            result['DomainBlacklistSchemaConfig'] = self.domain_blacklist_schema_config.to_map()

        if self.domain_whitelist_schema_config is not None:
            result['DomainWhitelistSchemaConfig'] = self.domain_whitelist_schema_config.to_map()

        if self.endpoint_hardening_schema_config is not None:
            result['EndpointHardeningSchemaConfig'] = self.endpoint_hardening_schema_config.to_map()

        if self.peripheral_block_schema_config is not None:
            result['PeripheralBlockSchemaConfig'] = self.peripheral_block_schema_config.to_map()

        if self.software_block_schema_config is not None:
            result['SoftwareBlockSchemaConfig'] = self.software_block_schema_config.to_map()

        if self.software_hardening_schema_config is not None:
            result['SoftwareHardeningSchemaConfig'] = self.software_hardening_schema_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUninstallSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfig()
            self.app_uninstall_schema_config = temp_model.from_map(m.get('AppUninstallSchemaConfig'))

        if m.get('DeviceRegistrationSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfig()
            self.device_registration_schema_config = temp_model.from_map(m.get('DeviceRegistrationSchemaConfig'))

        if m.get('DlpSendSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfig()
            self.dlp_send_schema_config = temp_model.from_map(m.get('DlpSendSchemaConfig'))

        if m.get('DomainBlacklistSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfig()
            self.domain_blacklist_schema_config = temp_model.from_map(m.get('DomainBlacklistSchemaConfig'))

        if m.get('DomainWhitelistSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfig()
            self.domain_whitelist_schema_config = temp_model.from_map(m.get('DomainWhitelistSchemaConfig'))

        if m.get('EndpointHardeningSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfig()
            self.endpoint_hardening_schema_config = temp_model.from_map(m.get('EndpointHardeningSchemaConfig'))

        if m.get('PeripheralBlockSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfig()
            self.peripheral_block_schema_config = temp_model.from_map(m.get('PeripheralBlockSchemaConfig'))

        if m.get('SoftwareBlockSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfig()
            self.software_block_schema_config = temp_model.from_map(m.get('SoftwareBlockSchemaConfig'))

        if m.get('SoftwareHardeningSchemaConfig') is not None:
            temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfig()
            self.software_hardening_schema_config = temp_model.from_map(m.get('SoftwareHardeningSchemaConfig'))

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareHardeningSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsSoftwareBlockSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsPeripheralBlockSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsEndpointHardeningSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsDomainWhitelistSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsDomainBlacklistSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsDlpSendSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsDeviceRegistrationSchemaConfigFieldMap(DaraModel):
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

class UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfig(DaraModel):
    def __init__(
        self,
        external_process_id: str = None,
        field_map: List[main_models.UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfigFieldMap] = None,
        schema_id: str = None,
    ):
        self.external_process_id = external_process_id
        self.field_map = field_map
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
                temp_model = main_models.UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfigFieldMap()
                self.field_map.append(temp_model.from_map(k1))

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

class UpdateApprovalProcessRequestMatchSchemaConfigsAppUninstallSchemaConfigFieldMap(DaraModel):
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

