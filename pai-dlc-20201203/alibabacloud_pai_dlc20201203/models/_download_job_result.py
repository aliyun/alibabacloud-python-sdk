# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DownloadJobResult(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        download_job_id: str = None,
        download_url: str = None,
        end_time: str = None,
        file_type: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        log_count: int = None,
        pod_ids: List[str] = None,
        pod_uids: List[str] = None,
        source_job_id: str = None,
        start_time: str = None,
        status: str = None,
        tenant_id: str = None,
        type: str = None,
        url_expire_time: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        self.display_name = display_name
        self.download_job_id = download_job_id
        self.download_url = download_url
        self.end_time = end_time
        self.file_type = file_type
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.log_count = log_count
        self.pod_ids = pod_ids
        self.pod_uids = pod_uids
        self.source_job_id = source_job_id
        self.start_time = start_time
        self.status = status
        self.tenant_id = tenant_id
        self.type = type
        self.url_expire_time = url_expire_time
        self.user_id = user_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.download_job_id is not None:
            result['DownloadJobId'] = self.download_job_id

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.log_count is not None:
            result['LogCount'] = self.log_count

        if self.pod_ids is not None:
            result['PodIds'] = self.pod_ids

        if self.pod_uids is not None:
            result['PodUids'] = self.pod_uids

        if self.source_job_id is not None:
            result['SourceJobId'] = self.source_job_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('DownloadJobId') is not None:
            self.download_job_id = m.get('DownloadJobId')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LogCount') is not None:
            self.log_count = m.get('LogCount')

        if m.get('PodIds') is not None:
            self.pod_ids = m.get('PodIds')

        if m.get('PodUids') is not None:
            self.pod_uids = m.get('PodUids')

        if m.get('SourceJobId') is not None:
            self.source_job_id = m.get('SourceJobId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

