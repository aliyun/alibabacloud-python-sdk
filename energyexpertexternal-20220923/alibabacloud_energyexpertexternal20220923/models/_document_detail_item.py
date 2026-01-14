# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentDetailItem(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        doc_hash: str = None,
        doc_name: str = None,
        doc_url: str = None,
        folder_id: str = None,
        folder_name: str = None,
        id: int = None,
        job_id: str = None,
        job_status: str = None,
        origin_doc_name: str = None,
        origin_doc_url: str = None,
        update_time: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        self.doc_hash = doc_hash
        self.doc_name = doc_name
        self.doc_url = doc_url
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.id = id
        self.job_id = job_id
        self.job_status = job_status
        self.origin_doc_name = origin_doc_name
        self.origin_doc_url = origin_doc_url
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.doc_hash is not None:
            result['docHash'] = self.doc_hash

        if self.doc_name is not None:
            result['docName'] = self.doc_name

        if self.doc_url is not None:
            result['docUrl'] = self.doc_url

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.folder_name is not None:
            result['folderName'] = self.folder_name

        if self.id is not None:
            result['id'] = self.id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.origin_doc_name is not None:
            result['originDocName'] = self.origin_doc_name

        if self.origin_doc_url is not None:
            result['originDocUrl'] = self.origin_doc_url

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('docHash') is not None:
            self.doc_hash = m.get('docHash')

        if m.get('docName') is not None:
            self.doc_name = m.get('docName')

        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('originDocName') is not None:
            self.origin_doc_name = m.get('originDocName')

        if m.get('originDocUrl') is not None:
            self.origin_doc_url = m.get('originDocUrl')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

