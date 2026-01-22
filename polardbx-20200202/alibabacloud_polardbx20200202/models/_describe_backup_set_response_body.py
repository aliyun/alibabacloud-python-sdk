# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupSetResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeBackupSetResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeBackupSetResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeBackupSetResponseBodyData(DaraModel):
    def __init__(
        self,
        backup_model: int = None,
        backup_set_id: int = None,
        backup_set_size: int = None,
        backup_type: int = None,
        begin_time: int = None,
        end_time: int = None,
        osslist: List[main_models.DescribeBackupSetResponseBodyDataOSSList] = None,
        status: int = None,
    ):
        self.backup_model = backup_model
        self.backup_set_id = backup_set_id
        self.backup_set_size = backup_set_size
        self.backup_type = backup_type
        self.begin_time = begin_time
        self.end_time = end_time
        self.osslist = osslist
        self.status = status

    def validate(self):
        if self.osslist:
            for v1 in self.osslist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_model is not None:
            result['BackupModel'] = self.backup_model

        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id

        if self.backup_set_size is not None:
            result['BackupSetSize'] = self.backup_set_size

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['OSSList'] = []
        if self.osslist is not None:
            for k1 in self.osslist:
                result['OSSList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupModel') is not None:
            self.backup_model = m.get('BackupModel')

        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')

        if m.get('BackupSetSize') is not None:
            self.backup_set_size = m.get('BackupSetSize')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.osslist = []
        if m.get('OSSList') is not None:
            for k1 in m.get('OSSList'):
                temp_model = main_models.DescribeBackupSetResponseBodyDataOSSList()
                self.osslist.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeBackupSetResponseBodyDataOSSList(DaraModel):
    def __init__(
        self,
        backup_set_file: str = None,
        download_link: str = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
    ):
        self.backup_set_file = backup_set_file
        self.download_link = download_link
        self.intranet_download_link = intranet_download_link
        self.link_expired_time = link_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_set_file is not None:
            result['BackupSetFile'] = self.backup_set_file

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetFile') is not None:
            self.backup_set_file = m.get('BackupSetFile')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        return self

