# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20210101 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupDataListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeBackupDataListResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeBackupDataListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBackupDataListResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeBackupDataListResponseBodyDataContent] = None,
        extra: str = None,
        page_number: int = None,
        page_size: int = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The information about the task.
        self.content = content
        # The additional information.
        self.extra = extra
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of backup sets.
        self.total_elements = total_elements
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeBackupDataListResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeBackupDataListResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        backup_download_url: str = None,
        backup_end_time: str = None,
        backup_id: str = None,
        backup_intranet_download_url: str = None,
        backup_location: str = None,
        backup_method: str = None,
        backup_mode: str = None,
        backup_name: str = None,
        backup_scale: str = None,
        backup_size: int = None,
        backup_start_time: str = None,
        backup_status: str = None,
        backup_type: str = None,
        checksum: str = None,
        consistent_time: int = None,
        encryption: str = None,
        engine: str = None,
        engine_version: str = None,
        expect_expire_time: str = None,
        expect_expire_type: str = None,
        instance_name: str = None,
        is_avail: int = None,
        polar_snapshot: main_models.DescribeBackupDataListResponseBodyDataContentPolarSnapshot = None,
        support_deletion: int = None,
    ):
        # The URL that is used to download the backup set over the Internet.
        # 
        # >  This parameter is returned only when the value of BackupMethod is **Physical** or **Logical**.
        self.backup_download_url = backup_download_url
        # The end time of the backup. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC.
        self.backup_end_time = backup_end_time
        # The ID of the backup set.
        self.backup_id = backup_id
        # The URL that is used to download the backup set over the internal network.
        # 
        # >  This parameter is returned only when the value of BackupMethod is **Physical** or **Logical**.
        self.backup_intranet_download_url = backup_intranet_download_url
        # The storage path of backup files.
        self.backup_location = backup_location
        # The backup method. Valid values:
        # 
        # *   **Physical**
        # *   **Logical**
        # *   **Snapshot**
        self.backup_method = backup_method
        # The backup mode. Valid values:
        # 
        # *   **Automated**
        # *   **Manual**
        self.backup_mode = backup_mode
        # The name of the backup set.
        self.backup_name = backup_name
        # The backup scale. Valid values:
        # 
        # *   **DBInstance**
        # *   **DBTable**
        self.backup_scale = backup_scale
        # The size of the backup set. Unit: byte.
        self.backup_size = backup_size
        # The start time of the backup. The time is in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC.
        self.backup_start_time = backup_start_time
        # The status of the backup set. Valid values:
        # 
        # *   **OK**: The backup succeeded.
        # *   **ERROR**: The backup failed.
        self.backup_status = backup_status
        # The backup type. Valid values:
        # 
        # *   **FullBackup**
        # *   **IncrementBackup**
        self.backup_type = backup_type
        # The checksum value.
        self.checksum = checksum
        # The snapshot checkpoint time. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.consistent_time = consistent_time
        # The information about the encryption.
        self.encryption = encryption
        # The type of the database engine.
        self.engine = engine
        # The engine version.
        self.engine_version = engine_version
        # The time when the backup set expires. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expect_expire_time = expect_expire_time
        # Indicates whether the backup set expires. Valid values:
        # 
        # *   NEVER: The backup set does not expire.
        # *   EXPIRED: The backup set expired.
        # *   DELAY: The backup set expires after a specific period of time.
        self.expect_expire_type = expect_expire_type
        # The instance ID.
        self.instance_name = instance_name
        # Indicates whether the backup set is available. Valid values:
        # 
        # *   **1**: The backup set is available.
        # *   **0**: The backup set is unavailable.
        self.is_avail = is_avail
        # The information about the PolarDB level-2 dump.
        # 
        # >  This parameter is returned only if the level-2 dump feature is enabled for the PolarDB for MySQL cluster and the level-1 backup is dumped.
        self.polar_snapshot = polar_snapshot
        # Indicates whether the backup set can be deleted. Valid values:
        # 
        # *   **0**: The backup set can be deleted.
        # *   **1**: The backup set cannot be deleted.
        self.support_deletion = support_deletion

    def validate(self):
        if self.polar_snapshot:
            self.polar_snapshot.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url

        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_intranet_download_url is not None:
            result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url

        if self.backup_location is not None:
            result['BackupLocation'] = self.backup_location

        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method

        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode

        if self.backup_name is not None:
            result['BackupName'] = self.backup_name

        if self.backup_scale is not None:
            result['BackupScale'] = self.backup_scale

        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.consistent_time is not None:
            result['ConsistentTime'] = self.consistent_time

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.expect_expire_type is not None:
            result['ExpectExpireType'] = self.expect_expire_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.is_avail is not None:
            result['IsAvail'] = self.is_avail

        if self.polar_snapshot is not None:
            result['PolarSnapshot'] = self.polar_snapshot.to_map()

        if self.support_deletion is not None:
            result['SupportDeletion'] = self.support_deletion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')

        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupIntranetDownloadURL') is not None:
            self.backup_intranet_download_url = m.get('BackupIntranetDownloadURL')

        if m.get('BackupLocation') is not None:
            self.backup_location = m.get('BackupLocation')

        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')

        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')

        if m.get('BackupName') is not None:
            self.backup_name = m.get('BackupName')

        if m.get('BackupScale') is not None:
            self.backup_scale = m.get('BackupScale')

        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('ConsistentTime') is not None:
            self.consistent_time = m.get('ConsistentTime')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('ExpectExpireType') is not None:
            self.expect_expire_type = m.get('ExpectExpireType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IsAvail') is not None:
            self.is_avail = m.get('IsAvail')

        if m.get('PolarSnapshot') is not None:
            temp_model = main_models.DescribeBackupDataListResponseBodyDataContentPolarSnapshot()
            self.polar_snapshot = temp_model.from_map(m.get('PolarSnapshot'))

        if m.get('SupportDeletion') is not None:
            self.support_deletion = m.get('SupportDeletion')

        return self

class DescribeBackupDataListResponseBodyDataContentPolarSnapshot(DaraModel):
    def __init__(
        self,
        dump_id: int = None,
        dump_size: int = None,
        expect_expire_time: str = None,
        expect_expire_type: str = None,
    ):
        # The dump backup ID.
        self.dump_id = dump_id
        # The size of the dump backup. Unit: byte.
        self.dump_size = dump_size
        # The time when the backup set expires. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.expect_expire_time = expect_expire_time
        # Indicates whether the backup set expires. Valid values:
        # 
        # *   NEVER: The backup set does not expire.
        # *   EXPIRED: The backup set expired.
        # *   DELAY: The backup set expires after a specific period of time.
        self.expect_expire_type = expect_expire_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dump_id is not None:
            result['DumpId'] = self.dump_id

        if self.dump_size is not None:
            result['DumpSize'] = self.dump_size

        if self.expect_expire_time is not None:
            result['ExpectExpireTime'] = self.expect_expire_time

        if self.expect_expire_type is not None:
            result['expectExpireType'] = self.expect_expire_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DumpId') is not None:
            self.dump_id = m.get('DumpId')

        if m.get('DumpSize') is not None:
            self.dump_size = m.get('DumpSize')

        if m.get('ExpectExpireTime') is not None:
            self.expect_expire_time = m.get('ExpectExpireTime')

        if m.get('expectExpireType') is not None:
            self.expect_expire_type = m.get('expectExpireType')

        return self

