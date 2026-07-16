# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMongoDBLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        enable_audit: bool = None,
        hot_ttl_for_v2standard: int = None,
        is_etl_meta_exist: int = None,
        is_user_project_logstore_exist: int = None,
        preserve_storage_for_standard: int = None,
        preserve_storage_for_trail: int = None,
        request_id: str = None,
        service_type: str = None,
        ttl_for_standard: int = None,
        ttl_for_trail: int = None,
        ttl_for_v2standard: int = None,
        used_storage_for_standard: int = None,
        used_storage_for_trail: int = None,
        user_project_name: str = None,
    ):
        # Indicates whether the audit log feature is enabled for the ApsaraDB for MongoDB instance.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_audit = enable_audit
        # The retention period of hot storage for the V2_Standard (DAS Enterprise Edition (NoSQL-compatible)) version of audit logs. Unit: days.
        self.hot_ttl_for_v2standard = hot_ttl_for_v2standard
        # Indicates whether a rule is created to ship audit logs to Logtail. For more information about Logtail, see [What is Logtail?](https://help.aliyun.com/document_detail/28979.html). Valid values:
        # 
        # - **1**: A rule is created.
        # 
        # - **0** or **null**: No rule is created.
        self.is_etl_meta_exist = is_etl_meta_exist
        # Indicates whether a Simple Log Service project for audit logs exists in the current region. Valid values:
        # 
        # - **1**: The project exists.
        # 
        # - **0** or **null**: The project does not exist.
        self.is_user_project_logstore_exist = is_user_project_logstore_exist
        # The maximum storage capacity for the official version of audit logs. A value of -1 indicates that no upper limit is set.
        self.preserve_storage_for_standard = preserve_storage_for_standard
        # The maximum storage capacity for the free trial version of audit logs. Unit: bytes. The maximum value is 107374182400 bytes.
        self.preserve_storage_for_trail = preserve_storage_for_trail
        # The request ID.
        self.request_id = request_id
        # The version of the audit log feature.
        # 
        # - **Trial**: Free trial version.
        # 
        # - **Standard**: Official version.
        # 
        # - **V2_Standard**: DAS Enterprise Edition (NoSQL-compatible) version.
        self.service_type = service_type
        # The retention period of audit logs for the official version. The value ranges from 1 to 365. Unit: days.
        self.ttl_for_standard = ttl_for_standard
        # The retention period of audit logs for the free trial version. Unit: days.
        self.ttl_for_trail = ttl_for_trail
        # The retention period of cold storage for the V2_Standard (DAS Enterprise Edition (NoSQL-compatible)) version of audit logs. Unit: days.
        self.ttl_for_v2standard = ttl_for_v2standard
        # The storage capacity that is used by audit logs for the official version. Unit: bytes.
        self.used_storage_for_standard = used_storage_for_standard
        # The storage capacity that is used by audit logs for the free trial version. Unit: bytes.
        self.used_storage_for_trail = used_storage_for_trail
        # The name of the Simple Log Service project for the audit logs.
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

        if self.hot_ttl_for_v2standard is not None:
            result['HotTtlForV2Standard'] = self.hot_ttl_for_v2standard

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

        if self.ttl_for_v2standard is not None:
            result['TtlForV2Standard'] = self.ttl_for_v2standard

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

        if m.get('HotTtlForV2Standard') is not None:
            self.hot_ttl_for_v2standard = m.get('HotTtlForV2Standard')

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

        if m.get('TtlForV2Standard') is not None:
            self.ttl_for_v2standard = m.get('TtlForV2Standard')

        if m.get('UsedStorageForStandard') is not None:
            self.used_storage_for_standard = m.get('UsedStorageForStandard')

        if m.get('UsedStorageForTrail') is not None:
            self.used_storage_for_trail = m.get('UsedStorageForTrail')

        if m.get('UserProjectName') is not None:
            self.user_project_name = m.get('UserProjectName')

        return self

