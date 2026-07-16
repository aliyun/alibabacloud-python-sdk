# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListBackupRecordResponseBody(DaraModel):
    def __init__(
        self,
        backup_record_list: List[main_models.ListBackupRecordResponseBodyBackupRecordList] = None,
        page_info: main_models.ListBackupRecordResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The list of backup records.
        self.backup_record_list = backup_record_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_record_list:
            for v1 in self.backup_record_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupRecordList'] = []
        if self.backup_record_list is not None:
            for k1 in self.backup_record_list:
                result['BackupRecordList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_record_list = []
        if m.get('BackupRecordList') is not None:
            for k1 in m.get('BackupRecordList'):
                temp_model = main_models.ListBackupRecordResponseBodyBackupRecordList()
                self.backup_record_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListBackupRecordResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBackupRecordResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries on the current page in a paged query.
        self.count = count
        # The page number of the current page in a paged query.
        self.current_page = current_page
        # The maximum number of entries per page in a paged query.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBackupRecordResponseBodyBackupRecordList(DaraModel):
    def __init__(
        self,
        backup_end_time: int = None,
        backup_job_id: str = None,
        backup_plan_id: str = None,
        backup_start_time: int = None,
        backup_status: str = None,
        client_id: str = None,
        error_code: str = None,
        error_message: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        region_id: str = None,
        uuid: str = None,
    ):
        # The backup end time. The value is a timestamp in milliseconds.
        self.backup_end_time = backup_end_time
        # The backup task ID.
        self.backup_job_id = backup_job_id
        # The backup plan ID.
        self.backup_plan_id = backup_plan_id
        # The backup start time. The value is a timestamp in milliseconds.
        self.backup_start_time = backup_start_time
        # The backup task status. Valid values:
        # - **BACKUP_COMPLETE**: backup succeeded
        # - **BACKUP_FAILED**: backup failed
        # - **PARTIAL_COMPLETE**: partial backup succeeded.
        self.backup_status = backup_status
        # The anti-ransomware client ID.
        self.client_id = client_id
        # The error code of the backup task.
        self.error_code = error_code
        # The error details of the backup task.
        self.error_message = error_message
        # The ID of the server instance.
        self.instance_id = instance_id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The IP address of the server.
        self.ip = ip
        # The region ID of the backup service.
        self.region_id = region_id
        # The UUID of the server backed up by database anti-ransomware.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time

        if self.backup_job_id is not None:
            result['BackupJobId'] = self.backup_job_id

        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time

        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')

        if m.get('BackupJobId') is not None:
            self.backup_job_id = m.get('BackupJobId')

        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')

        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

