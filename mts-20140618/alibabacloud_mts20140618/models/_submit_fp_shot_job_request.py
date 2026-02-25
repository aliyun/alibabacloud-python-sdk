# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitFpShotJobRequest(DaraModel):
    def __init__(
        self,
        fp_shot_config: str = None,
        input: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # The configurations of the media fingerprint analysis job. The value is a JSON object. For more information, see the "FpShotConfig" section of the [Parameter details](https://help.aliyun.com/document_detail/93568.html) topic.
        # 
        # This parameter is required.
        self.fp_shot_config = fp_shot_config
        # The OSS URL of the job input. The value is a JSON object. You can query the OSS URL in the OSS or MPS console.
        # 
        # > The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue. This ID can be used to associate the job with a notification method. To view the ID of the MPS queue, perform the following steps: Log on to the **MPS console**. In the left-side navigation pane, choose **Global Settings** > **Pipelines**.
        self.pipeline_id = pipeline_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The custom data. The value can be up to 128 bytes in length and cannot start with a special character.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fp_shot_config is not None:
            result['FpShotConfig'] = self.fp_shot_config

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
        if m.get('FpShotConfig') is not None:
            self.fp_shot_config = m.get('FpShotConfig')

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

