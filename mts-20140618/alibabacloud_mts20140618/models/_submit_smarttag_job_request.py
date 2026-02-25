# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSmarttagJobRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_addr: str = None,
        content_type: str = None,
        input: str = None,
        notify_url: str = None,
        owner_account: str = None,
        owner_id: int = None,
        params: str = None,
        pipeline_id: str = None,
        priority: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: str = None,
        title: str = None,
        user_data: str = None,
    ):
        self.content = content
        self.content_addr = content_addr
        self.content_type = content_type
        self.input = input
        self.notify_url = notify_url
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.params = params
        # This parameter is required.
        self.pipeline_id = pipeline_id
        # The priority of the job in the ApsaraVideo Media Processing (MPS) queue to which the job is added. Valid values: 0 to 9. Default value: 5.
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template ID, which is used to specify the analysis algorithm of the smart tagging job. For more information about how to manage templates, see [AddSmarttagTemplate](https://help.aliyun.com/document_detail/602910.html), [QuerySmarttagTemplateList](https://help.aliyun.com/document_detail/187770.html), [UpdateSmarttagTemplate](https://help.aliyun.com/document_detail/187776.html), and [DeleteSmarttagTemplate](https://help.aliyun.com/document_detail/187775.html).
        self.template_id = template_id
        # This parameter is required.
        self.title = title
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_addr is not None:
            result['ContentAddr'] = self.content_addr

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.input is not None:
            result['Input'] = self.input

        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.params is not None:
            result['Params'] = self.params

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentAddr') is not None:
            self.content_addr = m.get('ContentAddr')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

