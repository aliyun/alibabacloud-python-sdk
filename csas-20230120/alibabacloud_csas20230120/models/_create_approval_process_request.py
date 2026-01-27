# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateApprovalProcessRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        match_schemas: main_models.CreateApprovalProcessRequestMatchSchemas = None,
        process_name: str = None,
        process_nodes: List[List[str]] = None,
    ):
        self.description = description
        self.match_schemas = match_schemas
        # This parameter is required.
        self.process_name = process_name
        # This parameter is required.
        self.process_nodes = process_nodes

    def validate(self):
        if self.match_schemas:
            self.match_schemas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.match_schemas is not None:
            result['MatchSchemas'] = self.match_schemas.to_map()

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_nodes is not None:
            result['ProcessNodes'] = self.process_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchSchemas') is not None:
            temp_model = main_models.CreateApprovalProcessRequestMatchSchemas()
            self.match_schemas = temp_model.from_map(m.get('MatchSchemas'))

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessNodes') is not None:
            self.process_nodes = m.get('ProcessNodes')

        return self

class CreateApprovalProcessRequestMatchSchemas(DaraModel):
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

