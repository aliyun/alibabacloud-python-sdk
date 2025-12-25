# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledPreloadJobResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        created_at: str = None,
        domains: str = None,
        error_info: str = None,
        failed_file_oss: str = None,
        file_id: str = None,
        id: str = None,
        insert_way: str = None,
        name: str = None,
        request_id: str = None,
        site_id: int = None,
        task_submitted: int = None,
        task_type: str = None,
        url_count: int = None,
        url_submitted: int = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The time when the task was created.
        self.created_at = created_at
        # The domain names to be prefetched.
        self.domains = domains
        # The error message. Multiple error messages are separated by commas (,). Valid values:
        # 
        # *   **InvalidUrl**: The URL format is invalid.
        # *   **InvalidDomain**: The domain name fails the domain ownership verification.
        # *   **QuotaExcess**: the quota limit has been reached.
        # *   **OtherErrors**: other errors.
        self.error_info = error_info
        # The URL of the OSS object that stores a list of URLs that failed the conditional check for prefetching.
        self.failed_file_oss = failed_file_oss
        # The ID of the URL list file, which can be used during downloads.
        self.file_id = file_id
        # The ID of the scheduled prefetch task.
        self.id = id
        # The method to submit the URLs to be prefetched.
        self.insert_way = insert_way
        # The task name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The website ID.
        self.site_id = site_id
        # The number of submitted prefetch tasks.
        self.task_submitted = task_submitted
        # The task type (refresh or preload).
        self.task_type = task_type
        # The total number of URLs.
        self.url_count = url_count
        # The number of submitted URLs.
        self.url_submitted = url_submitted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.domains is not None:
            result['Domains'] = self.domains

        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info

        if self.failed_file_oss is not None:
            result['FailedFileOss'] = self.failed_file_oss

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.id is not None:
            result['Id'] = self.id

        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.task_submitted is not None:
            result['TaskSubmitted'] = self.task_submitted

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.url_count is not None:
            result['UrlCount'] = self.url_count

        if self.url_submitted is not None:
            result['UrlSubmitted'] = self.url_submitted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')

        if m.get('FailedFileOss') is not None:
            self.failed_file_oss = m.get('FailedFileOss')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TaskSubmitted') is not None:
            self.task_submitted = m.get('TaskSubmitted')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UrlCount') is not None:
            self.url_count = m.get('UrlCount')

        if m.get('UrlSubmitted') is not None:
            self.url_submitted = m.get('UrlSubmitted')

        return self

