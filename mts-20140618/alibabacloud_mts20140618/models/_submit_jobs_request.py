# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitJobsRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        output_bucket: str = None,
        output_location: str = None,
        outputs: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The information about the input file. For more information, see the "Input" section of the [Parameter details](https://help.aliyun.com/document_detail/29253.html) topic.
        # 
        # > 
        # 
        # *   The path of an Object Storage Service (OSS) object must be URL-encoded in UTF-8 before you use the path in MPS.
        # 
        # *   The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        # The name of the OSS bucket that stores the output file.
        # 
        # *   For more information about the term bucket, see [Terms](https://help.aliyun.com/document_detail/31827.html).
        # 
        # This parameter is required.
        self.output_bucket = output_bucket
        # The region in which the OSS bucket that stores the output file resides.
        # 
        # *   The OSS bucket must reside in the same region as MPS.
        # *   For more information about the term bucket, see [Terms](https://help.aliyun.com/document_detail/31827.html).
        self.output_location = output_location
        # The job output configurations. For more information, see the "Output" section of the [Parameter details](https://help.aliyun.com/document_detail/29253.html) topic.
        # 
        # *   Specify the value in a JSON array of Output objects. You can specify up to 30 Output objects.
        # 
        # This parameter is required.
        self.outputs = outputs
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue. For more information, see [Terms](https://help.aliyun.com/document_detail/31827.html).
        # 
        # *   To obtain the ID of an MPS queue, you can log on to the [MPS console](https://mps.console.aliyun.com/overview) and choose **Global Settings** > **MPS Queue and Callback** in the left-side navigation pane.
        # *   If you want to receive asynchronous message notifications, associate an MNS queue or topic with the MPS queue. For more information, see [Receive notifications](https://help.aliyun.com/document_detail/42618.html).
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.output_bucket is not None:
            result['OutputBucket'] = self.output_bucket

        if self.output_location is not None:
            result['OutputLocation'] = self.output_location

        if self.outputs is not None:
            result['Outputs'] = self.outputs

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('OutputBucket') is not None:
            self.output_bucket = m.get('OutputBucket')

        if m.get('OutputLocation') is not None:
            self.output_location = m.get('OutputLocation')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

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

        return self

