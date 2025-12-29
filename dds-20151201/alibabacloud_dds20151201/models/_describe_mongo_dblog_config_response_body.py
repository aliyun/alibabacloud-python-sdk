# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMongoDBLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        enable_audit: bool = None,
        is_etl_meta_exist: int = None,
        is_user_project_logstore_exist: int = None,
        preserve_storage_for_standard: int = None,
        preserve_storage_for_trail: int = None,
        request_id: str = None,
        service_type: str = None,
        ttl_for_standard: int = None,
        ttl_for_trail: int = None,
        used_storage_for_standard: int = None,
        used_storage_for_trail: int = None,
        user_project_name: str = None,
    ):
        # Indicates whether to enable the audit log feature.
        # 
        # *   **true**: The audit log feature is enabled.
        # *   **false**: The audit log feature is disabled.
        self.enable_audit = enable_audit
        # Indicates whether a rule to distribute logs to Logtail is created. For more information, see [Logtail overview](https://help.aliyun.com/document_detail/28979.html). Valid values:
        # 
        # *   **1**: A rule to distribute logs to Logtail is created.
        # *   **0** or **null**: A rule to distribute logs to Logtail is not created.
        self.is_etl_meta_exist = is_etl_meta_exist
        # Indicates whether a project exists in the current region. Valid values:
        # 
        # *   **1**: A logging project exists in the current region.
        # *   **0** or **null**: A logging project does not exist in the current region.
        self.is_user_project_logstore_exist = is_user_project_logstore_exist
        # The maximum storage capacity for the formal edition of the audit log feature. If the value is -1, no maximum storage capacity is set.
        self.preserve_storage_for_standard = preserve_storage_for_standard
        # The maximum storage capacity for the free trial edition of the audit log feature. Unit: bytes. You can set the maximum storage capacity to 107,374,182,400 bytes.
        self.preserve_storage_for_trail = preserve_storage_for_trail
        # The request ID.
        self.request_id = request_id
        # The type of the audit log feature. Valid values:
        # 
        # *   **Trail**: the free trial edition
        # *   **Standard**: the official edition
        self.service_type = service_type
        # The retention period for the official edition of the audit log feature. Valid values: 1 to 365. Unit: day.
        self.ttl_for_standard = ttl_for_standard
        # The retention period for the free trial edition of the audit log feature.
        self.ttl_for_trail = ttl_for_trail
        # The used storage capacity for the formal edition of the audit log feature. Unit: bytes.
        self.used_storage_for_standard = used_storage_for_standard
        # The used storage capacity for the free trial edition of the audit log feature. Unit: bytes.
        self.used_storage_for_trail = used_storage_for_trail
        # The name of the project.
        self.user_project_name = user_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit

        if self.is_etl_meta_exist is not None:
            result['IsEtlMetaExist'] = self.is_etl_meta_exist

        if self.is_user_project_logstore_exist is not None:
            result['IsUserProjectLogstoreExist'] = self.is_user_project_logstore_exist

        if self.preserve_storage_for_standard is not None:
            result['PreserveStorageForStandard'] = self.preserve_storage_for_standard

        if self.preserve_storage_for_trail is not None:
            result['PreserveStorageForTrail'] = self.preserve_storage_for_trail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.ttl_for_standard is not None:
            result['TtlForStandard'] = self.ttl_for_standard

        if self.ttl_for_trail is not None:
            result['TtlForTrail'] = self.ttl_for_trail

        if self.used_storage_for_standard is not None:
            result['UsedStorageForStandard'] = self.used_storage_for_standard

        if self.used_storage_for_trail is not None:
            result['UsedStorageForTrail'] = self.used_storage_for_trail

        if self.user_project_name is not None:
            result['UserProjectName'] = self.user_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')

        if m.get('IsEtlMetaExist') is not None:
            self.is_etl_meta_exist = m.get('IsEtlMetaExist')

        if m.get('IsUserProjectLogstoreExist') is not None:
            self.is_user_project_logstore_exist = m.get('IsUserProjectLogstoreExist')

        if m.get('PreserveStorageForStandard') is not None:
            self.preserve_storage_for_standard = m.get('PreserveStorageForStandard')

        if m.get('PreserveStorageForTrail') is not None:
            self.preserve_storage_for_trail = m.get('PreserveStorageForTrail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('TtlForStandard') is not None:
            self.ttl_for_standard = m.get('TtlForStandard')

        if m.get('TtlForTrail') is not None:
            self.ttl_for_trail = m.get('TtlForTrail')

        if m.get('UsedStorageForStandard') is not None:
            self.used_storage_for_standard = m.get('UsedStorageForStandard')

        if m.get('UsedStorageForTrail') is not None:
            self.used_storage_for_trail = m.get('UsedStorageForTrail')

        if m.get('UserProjectName') is not None:
            self.user_project_name = m.get('UserProjectName')

        return self

