# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIImageAuditJobRequest(DaraModel):
    def __init__(
        self,
        censor_provider: str = None,
        image_service: str = None,
        media_audit_configuration: str = None,
        media_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        service_parameters: str = None,
        template_id: str = None,
    ):
        self.censor_provider = censor_provider
        self.image_service = image_service
        # The review node configuration.
        # - Other configuration items of the review node. Currently, only the ResourceType field is supported, which is used to specify the media file type. You can adjust the review standards and rules for the specified type.
        # - Usage notes for ResourceType: Only letters, digits, and underscores (_) are allowed.
        # 
        # >- You can customize the ResourceType field based on the usage notes. After customization, [submit a Yida form](https://yida.alibaba-inc.com/o/ticketapply) to commit to Alibaba Cloud for spooling before the configuration takes effect.
        # >- To adjust the review standards and rules for a specific ResourceType, [submit a Yida form](https://yida.alibaba-inc.com/o/ticketapply) to request technical support.
        self.media_audit_configuration = media_audit_configuration
        # The image ID.
        # 
        # The unique identifier of the image returned after the image is uploaded to ApsaraVideo VOD.
        # 
        # This parameter is required.
        self.media_id = media_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.service_parameters = service_parameters
        # The AI template ID. You can obtain the ID by using one of the following methods:
        # - Call the [Add AI template](https://help.aliyun.com/document_detail/102930.html) operation to add an AI template. The AI template ID is the value of TemplateId in the response.
        # - After the AI template is added, call the [Query AI template list](https://help.aliyun.com/document_detail/102936.html) operation to query the AI template ID, which is the value of TemplateId in the response.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.censor_provider is not None:
            result['CensorProvider'] = self.censor_provider

        if self.image_service is not None:
            result['ImageService'] = self.image_service

        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CensorProvider') is not None:
            self.censor_provider = m.get('CensorProvider')

        if m.get('ImageService') is not None:
            self.image_service = m.get('ImageService')

        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

