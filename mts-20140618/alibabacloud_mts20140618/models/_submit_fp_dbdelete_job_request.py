# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitFpDBDeleteJobRequest(DaraModel):
    def __init__(
        self,
        del_type: str = None,
        fp_dbid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # The operation type. Valid values:
        # 
        # *   **Purge**: clears the media fingerprint library. The content in the library is deleted, but the library is not deleted.
        # *   **Delete**: deletes the media fingerprint library. Both the library and its content are deleted.
        # *   Default value: **Purge**.
        self.del_type = del_type
        # The ID of the media fingerprint library. You can obtain the library ID from the response parameters of the [CreateFpShotDB](https://help.aliyun.com/document_detail/170149.html) operation.
        # 
        # This parameter is required.
        self.fp_dbid = fp_dbid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the ApsaraVideo Media Processing (MPS) queue. This ID can be used to associate the job with a notification method. To view the MPS queue ID, log on to the **MPS console** and choose **Global Settings** > **Pipelines** in the left-side navigation pane.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The custom data. The value can contain letters and digits and can be up to 128 bytes in length.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.del_type is not None:
            result['DelType'] = self.del_type

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelType') is not None:
            self.del_type = m.get('DelType')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

