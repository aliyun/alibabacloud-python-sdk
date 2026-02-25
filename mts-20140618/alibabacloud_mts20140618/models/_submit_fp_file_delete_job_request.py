# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitFpFileDeleteJobRequest(DaraModel):
    def __init__(
        self,
        file_ids: str = None,
        fp_dbid: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        primary_keys: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # The IDs of the media files that you want to delete. Separate multiple file IDs with commas (,). You can delete up to 200 media files at a time. You can obtain media file IDs from the response parameters of the [ListFpShotFiles](https://help.aliyun.com/document_detail/209266.html) operation.
        self.file_ids = file_ids
        # The ID of the media fingerprint library. You can obtain the library ID from the response parameters of the [CreateFpShotDB](https://help.aliyun.com/document_detail/170149.html) operation.
        # 
        # This parameter is required.
        self.fp_dbid = fp_dbid
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the ApsaraVideo Media Processing (MPS) queue to which the job is submitted. The MPS queue is bound with a notification method. To view the MPS queue ID, log on to the **MPS console** and choose **Global Settings** > **MPS queue and Callback** in the left-side navigation pane.
        self.pipeline_id = pipeline_id
        # The primary keys of the files to be deleted. Separate multiple primary keys with commas (,). You can delete up to 200 primary keys at a time. You can obtain the primary keys of media files from the response parameters of the [ListFpShotFiles](https://help.aliyun.com/document_detail/209266.html) operation.
        # 
        # >  This parameter is available only in the China (Beijing), China (Hangzhou), and China (Shanghai) regions.
        self.primary_keys = primary_keys
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
        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.fp_dbid is not None:
            result['FpDBId'] = self.fp_dbid

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('FpDBId') is not None:
            self.fp_dbid = m.get('FpDBId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

