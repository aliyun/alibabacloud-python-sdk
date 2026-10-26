# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupLogDownloadLinksResponseBody(DaraModel):
    def __init__(
        self,
        backup_log_download_link_item: List[main_models.DescribeBackupLogDownloadLinksResponseBodyBackupLogDownloadLinkItem] = None,
        request_id: str = None,
    ):
        # The details of the redo log backups.
        self.backup_log_download_link_item = backup_log_download_link_item
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.backup_log_download_link_item:
            for v1 in self.backup_log_download_link_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupLogDownloadLinkItem'] = []
        if self.backup_log_download_link_item is not None:
            for k1 in self.backup_log_download_link_item:
                result['BackupLogDownloadLinkItem'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_log_download_link_item = []
        if m.get('BackupLogDownloadLinkItem') is not None:
            for k1 in m.get('BackupLogDownloadLinkItem'):
                temp_model = main_models.DescribeBackupLogDownloadLinksResponseBodyBackupLogDownloadLinkItem()
                self.backup_log_download_link_item.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupLogDownloadLinksResponseBodyBackupLogDownloadLinkItem(DaraModel):
    def __init__(
        self,
        backup_log_id: str = None,
        download_link: str = None,
        error_code: str = None,
        intranet_download_link: str = None,
        link_expired_time: str = None,
        message: str = None,
    ):
        # The ID of the redo log backup.
        self.backup_log_id = backup_log_id
        # The public download link for the redo log backup.
        self.download_link = download_link
        # The error code for the individual record. Empty if the request is successful.
        self.error_code = error_code
        # The internal network download link for the redo log backup.
        self.intranet_download_link = intranet_download_link
        # The expiration time of the download link in UTC.
        self.link_expired_time = link_expired_time
        # The error message for the individual record. Empty if the request is successful.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_log_id is not None:
            result['BackupLogId'] = self.backup_log_id

        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.intranet_download_link is not None:
            result['IntranetDownloadLink'] = self.intranet_download_link

        if self.link_expired_time is not None:
            result['LinkExpiredTime'] = self.link_expired_time

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupLogId') is not None:
            self.backup_log_id = m.get('BackupLogId')

        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('IntranetDownloadLink') is not None:
            self.intranet_download_link = m.get('IntranetDownloadLink')

        if m.get('LinkExpiredTime') is not None:
            self.link_expired_time = m.get('LinkExpiredTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

