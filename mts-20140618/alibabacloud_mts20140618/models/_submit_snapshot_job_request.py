# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSnapshotJobRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_config: str = None,
        user_data: str = None,
    ):
        # The information about the job input. The value must be a JSON object. You must add the Object Storage Service (OSS) bucket that stores the OSS object to be used as the job input as a media bucket in the MPS console. To add an OSS bucket as a media bucket, you can log on to the MPS console, choose Workflows > Media Buckets in the left-side navigation pane, and then click Add Bucket. After the OSS bucket is added as a media bucket, you must perform URL encoding for the OSS object. Example: `{"Bucket":"example-bucket","Location":"example-location","Object":"example%2Ftest.flv"}`. This example indicates the `"example-bucket.example-location.aliyuncs.com/example/test.flv"` object.
        # 
        # > The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue to which you want to submit the snapshot job. To obtain the ID, you can log on to the **MPS console** and choose **Global Settings** > **Pipelines** in the left-side navigation pane.
        # 
        # > Make sure that an available Message Service (MNS) topic is bound to the specified MPS queue. Otherwise, the relevant messages may fail to be sent as expected.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot configurations. For more information, see the "AliyunSnapshotConfig" section of the [Data types](https://help.aliyun.com/document_detail/29253.html) topic.
        # 
        # > If you set the Interval parameter that is nested under SnapshotConfig, snapshots are captured at the specified intervals. The default value of the Interval parameter is 10, in seconds. If an input video is short but you specify large values for both the Num and Interval parameters, the actual number of snapshots captured may be smaller than the specified number. For example, if you set the Num parameter to 5 and the Interval parameter to 3 for a video of 10 seconds, the number of snapshots captured cannot reach 5.
        # 
        # This parameter is required.
        self.snapshot_config = snapshot_config
        # The custom data. The custom data can contain letters, digits, and hyphens (-) and be up to 1,024 bytes in size. The custom data cannot start with a special character.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

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

        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

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

        if m.get('SnapshotConfig') is not None:
            self.snapshot_config = m.get('SnapshotConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

