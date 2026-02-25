# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaInfoJobRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        config: str = None,
        input: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # Specifies whether to enable the asynchronous mode for the job. We recommend that you set this parameter to true. Valid values:
        # 
        # *   **true**: enables the asynchronous mode.
        # *   **false**: does not enable the asynchronous mode.
        self.async_ = async_
        self.config = config
        # The information about the input media file. The value is a JSON string. You must perform the following operations to add the OSS bucket in which the input media file is stored as a media bucket: Log on to the **MPS console**, choose **Workflows** > **Media Buckets** in the left-side navigation pane, and then click **Add Bucket**. After you add the OSS bucket as a media bucket, you must perform URL encoding for the OSS object. For example, `{"Bucket":"example-bucket","Location":"example-location","Object":"example%2Fexample.flv"}` indicates the `example-bucket.example-location.aliyuncs.com/example/example.flv` file.
        # 
        # > The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue to which the job was submitted. For more information, see [Terms](https://help.aliyun.com/document_detail/29197.html).
        # 
        # *   To view the ID of the MPS queue, log on to the [MPS console](https://mps.console.aliyun.com/overview) and choose **Global Settings** > **MPS queue and Callback** in the left-side navigation pane. On the MPS queue and Callback page, you can view the ID of an MPS queue or create an MPS queue.
        # *   If you want to receive asynchronous message notifications, associate an MNS queue or topic with the MPS queue. For more information, see [Receive message notifications](https://www.alibabacloud.com/help/en/mps/receive-message-notifications/?spm=a2c63.p38356.0.0.b48576d2jxNSca).
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The custom data. The custom data can contain letters, digits, and hyphens (-), and can be up to 1,024 bytes in length. The custom data cannot start with a special character.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.config is not None:
            result['Config'] = self.config

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

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('Config') is not None:
            self.config = m.get('Config')

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

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

