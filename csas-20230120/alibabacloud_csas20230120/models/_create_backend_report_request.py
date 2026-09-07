# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateBackendReportRequest(DaraModel):
    def __init__(
        self,
        end_timestamp: int = None,
        policy_type: str = None,
        reason: str = None,
        report_objects: List[main_models.CreateBackendReportRequestReportObjects] = None,
        targets: List[main_models.CreateBackendReportRequestTargets] = None,
        validity_type: str = None,
    ):
        # The filing expiration time as a UNIX timestamp in seconds. This parameter is required when ValidityType is set to FixedTime or ValidityType is not specified, and the value must be later than the current time. When ValidityType is set to Permanent, do not specify this parameter or set it to 0.
        self.end_timestamp = end_timestamp
        # The filing policy type. Valid values:
        # * PrivateAccessBlock: private access.
        # * DomainWhitelist: domain name whitelist.
        # * DomainBlacklist: domain name blacklist.
        # * SoftwareBlock: software blocking.
        # * DlpSend: file outbound transfer.
        # * PeripheralBlock: peripheral control.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The filing reason. The value must be 1 to 1024 characters in length.
        # 
        # This parameter is required.
        self.reason = reason
        # The list of filing objects, serialized in Flat format. You can specify 1 to 100 filing objects of the same policy type. The object fields must match the PolicyType value.
        # 
        # This parameter is required.
        self.report_objects = report_objects
        # The list of filing users, serialized in Flat format. You can specify 1 to 100 users. Only specific SASE users under the current Alibaba Cloud account are supported. The product of the number of deduplicated users and the number of filing objects cannot exceed 100.
        # 
        # This parameter is required.
        self.targets = targets
        # The validity duration type. Default value: FixedTime. Valid values:
        # * FixedTime: Expires at the specified time.
        # * Permanent: Permanently valid.
        self.validity_type = validity_type

    def validate(self):
        if self.report_objects:
            for v1 in self.report_objects:
                 if v1:
                    v1.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.reason is not None:
            result['Reason'] = self.reason

        result['ReportObjects'] = []
        if self.report_objects is not None:
            for k1 in self.report_objects:
                result['ReportObjects'].append(k1.to_map() if k1 else None)

        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        self.report_objects = []
        if m.get('ReportObjects') is not None:
            for k1 in m.get('ReportObjects'):
                temp_model = main_models.CreateBackendReportRequestReportObjects()
                self.report_objects.append(temp_model.from_map(k1))

        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.CreateBackendReportRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')

        return self

class CreateBackendReportRequestTargets(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The SASE user ID. You can call ListUsers to query the ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class CreateBackendReportRequestReportObjects(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        dev_type: str = None,
        device_type: str = None,
        file_md_5: str = None,
        report_domain: str = None,
        scope: str = None,
        software_id: str = None,
    ):
        # The private access application ID. This parameter is required when PolicyType is set to PrivateAccessBlock. You can call ListPrivateAccessApplications to query the ID.
        self.application_id = application_id
        # The endpoint operating system. This parameter is required when PolicyType is set to PeripheralBlock. Valid values:
        # * windows: Windows.
        # * macOS: macOS.
        self.dev_type = dev_type
        # The peripheral channel. This parameter is required when PolicyType is set to PeripheralBlock. Windows supports usbStorage, printer, mobile, cardReader, cdrom, and bluetooth. macOS supports usbStorage, airDrop, mobile, and bluetooth.
        self.device_type = device_type
        # The file MD5 hash. This parameter is required when PolicyType is set to DlpSend. The value must be a 32-character hexadecimal string and is case-insensitive.
        self.file_md_5 = file_md_5
        # The filing domain name. This parameter is required when PolicyType is set to DomainWhitelist or DomainBlacklist. Regular domain names and wildcard domain names that start with *. are supported. Protocols, ports, and paths are not supported.
        self.report_domain = report_domain
        # The peripheral filing granularity. This parameter is required when PolicyType is set to PeripheralBlock. Currently, only Channel is supported, which indicates filing by peripheral channel.
        self.scope = scope
        # The blocked software ID. This parameter is required when PolicyType is set to SoftwareBlock.
        self.software_id = software_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.report_domain is not None:
            result['ReportDomain'] = self.report_domain

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('ReportDomain') is not None:
            self.report_domain = m.get('ReportDomain')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        return self

