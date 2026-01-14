# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataLimitRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auto_scan: int = None,
        certificate_permission: str = None,
        enable: int = None,
        engine_type: str = None,
        event_status: int = None,
        feature_type: int = None,
        instantly_scan: bool = None,
        lang: str = None,
        log_store_day: int = None,
        ocr_status: int = None,
        parent_id: str = None,
        password: str = None,
        port: int = None,
        resource_type: int = None,
        sampling_size: int = None,
        service_region_id: str = None,
        source_ip: str = None,
        user_name: str = None,
    ):
        # Specifies whether to enable the security audit feature. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.audit_status = audit_status
        # Specifies whether to automatically trigger a re-scan after a rule is modified. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        # 
        # > When a re-scan is triggered, DSC scans all data in your data asset.
        self.auto_scan = auto_scan
        # The permissions. Valid values:
        # 
        # *   **ReadOnly**: read-only permissions
        # *   **ReadWrite**: read and write permissions
        self.certificate_permission = certificate_permission
        # Specifies whether to enable sensitive data detection. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        # 
        # > If this is your first time to authorize DSC to access the data asset, the default value is 1. If this is not your first time to authorize DSC to access the data asset, the default value is the same as that used in the last authorization operation. Both 1 and 0 are possible.
        self.enable = enable
        # The database engine that is run by the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        self.engine_type = engine_type
        # Specifies whether to enable anomalous event detection. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes (default)
        self.event_status = event_status
        # This parameter is deprecated.
        self.feature_type = feature_type
        # Specifies whether to immediately scan the authorized asset. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.instantly_scan = instantly_scan
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang
        # The retention period of raw logs after you enable the security audit feature. Unit: days. Valid values:
        # 
        # *   **30**
        # *   **90**
        # *   **180**
        # *   **365**
        self.log_store_day = log_store_day
        # Specifies whether to enable optical character recognition (OCR). Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.ocr_status = ocr_status
        # The name of the asset. The value is a connection string. It consists of an instance ID and a database name, which are separated by a comma (,). This parameter is required.
        self.parent_id = parent_id
        # The password that is used to access the database.
        self.password = password
        # The port that is used to connect to the database.
        self.port = port
        # The type of service to which the data asset belongs. Valid values:
        # 
        # *   **1** :MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4** :Tablestore
        # *   **5**: ApsaraDB RDS
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The number of sensitive data samples that are collected after sensitive data detection is enabled. Valid values:
        # 
        # *   **0**
        # *   **5**
        # *   **10**
        self.sampling_size = sampling_size
        # The region in which the data asset resides. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing).
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-huhehaote**: China (Hohhot)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        self.service_region_id = service_region_id
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The username that is used to access the database.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.auto_scan is not None:
            result['AutoScan'] = self.auto_scan

        if self.certificate_permission is not None:
            result['CertificatePermission'] = self.certificate_permission

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.instantly_scan is not None:
            result['InstantlyScan'] = self.instantly_scan

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_store_day is not None:
            result['LogStoreDay'] = self.log_store_day

        if self.ocr_status is not None:
            result['OcrStatus'] = self.ocr_status

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sampling_size is not None:
            result['SamplingSize'] = self.sampling_size

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AutoScan') is not None:
            self.auto_scan = m.get('AutoScan')

        if m.get('CertificatePermission') is not None:
            self.certificate_permission = m.get('CertificatePermission')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('InstantlyScan') is not None:
            self.instantly_scan = m.get('InstantlyScan')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogStoreDay') is not None:
            self.log_store_day = m.get('LogStoreDay')

        if m.get('OcrStatus') is not None:
            self.ocr_status = m.get('OcrStatus')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SamplingSize') is not None:
            self.sampling_size = m.get('SamplingSize')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

