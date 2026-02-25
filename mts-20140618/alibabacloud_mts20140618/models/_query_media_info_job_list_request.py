# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMediaInfoJobListRequest(DaraModel):
    def __init__(
        self,
        media_info_job_ids: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The IDs of the media information analysis jobs.
        # 
        # *   You can query up to 10 jobs at a time. Separate multiple IDs with commas (,).
        # *   You can obtain the details from the response parameters of the [SubmitMediaInfoJob](https://help.aliyun.com/document_detail/602827.html) operation.
        # 
        # >  If you do not specify the JobIds parameter, the **InvalidParameter** error code is returned.
        # 
        # This parameter is required.
        self.media_info_job_ids = media_info_job_ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_info_job_ids is not None:
            result['MediaInfoJobIds'] = self.media_info_job_ids

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaInfoJobIds') is not None:
            self.media_info_job_ids = m.get('MediaInfoJobIds')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

