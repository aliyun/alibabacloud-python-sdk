# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAnalysisJobRequest(DaraModel):
    def __init__(
        self,
        analysis_config: str = None,
        input: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        priority: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_data: str = None,
    ):
        # The job configurations. Set this parameter as required. For more information, see the "AnalysisConfig" section of the [Parameter details](https://help.aliyun.com/document_detail/29253.html) topic.
        self.analysis_config = analysis_config
        # The input information about the preset template analysis job to be submitted. The value must be a JSON object. You must log on to the Object Storage Service (OSS) console to grant the read permissions on the specified OSS bucket to MPS. For more information, see the "Input" section of the [Parameter details](https://help.aliyun.com/document_detail/29253.html) topic.
        # 
        # > The OSS bucket must reside in the same region as your MPS service.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the MPS queue to which the job is submitted. To view the ID of the MPS queue, log on to the **MPS console** and choose **Global Settings** > **Pipelines** in the left-side navigation pane. If you want to enable asynchronous notifications, make sure that the MPS queue is bound to a Message Service (MNS) topic.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # The priority of the job in the MPS queue to which the job is submitted.
        # 
        # *   Valid values: **1 to 10**. A value of 10 indicates the highest priority.
        # *   Default value: **6**.
        self.priority = priority
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
        if self.analysis_config is not None:
            result['AnalysisConfig'] = self.analysis_config

        if self.input is not None:
            result['Input'] = self.input

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisConfig') is not None:
            self.analysis_config = m.get('AnalysisConfig')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

