# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceShareResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share: main_models.UpdateResourceShareResponseBodyResourceShare = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information of the resource share.
        self.resource_share = resource_share

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceShare') is not None:
            temp_model = main_models.UpdateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m.get('ResourceShare'))

        return self

class UpdateResourceShareResponseBodyResourceShare(DaraModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        resource_share_status: str = None,
        update_time: str = None,
    ):
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets
        # The time when the resource share was created.
        self.create_time = create_time
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The owner of the resource share.
        self.resource_share_owner = resource_share_owner
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status
        # The time when the resource share was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner

        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')

        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

