# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolarOSSAuthorizedAccountResponseBody(DaraModel):
    def __init__(
        self,
        authorized_user_arn_ids: str = None,
        authorized_user_ids: str = None,
        pfs_instance_id: str = None,
        request_id: str = None,
    ):
        # The updated list of RAM role ARNs, separated by commas.
        self.authorized_user_arn_ids = authorized_user_arn_ids
        # The updated list of UIDs, separated by commas.
        self.authorized_user_ids = authorized_user_ids
        # The cold storage instance ID.
        self.pfs_instance_id = pfs_instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_user_arn_ids is not None:
            result['AuthorizedUserArnIds'] = self.authorized_user_arn_ids

        if self.authorized_user_ids is not None:
            result['AuthorizedUserIds'] = self.authorized_user_ids

        if self.pfs_instance_id is not None:
            result['PfsInstanceId'] = self.pfs_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedUserArnIds') is not None:
            self.authorized_user_arn_ids = m.get('AuthorizedUserArnIds')

        if m.get('AuthorizedUserIds') is not None:
            self.authorized_user_ids = m.get('AuthorizedUserIds')

        if m.get('PfsInstanceId') is not None:
            self.pfs_instance_id = m.get('PfsInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

