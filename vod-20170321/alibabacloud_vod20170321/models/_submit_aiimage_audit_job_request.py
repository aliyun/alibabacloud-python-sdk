# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIImageAuditJobRequest(DaraModel):
    def __init__(
        self,
        media_audit_configuration: str = None,
        media_id: str = None,
        owner_account: str = None,
        owner_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        template_id: str = None,
    ):
        # The configuration information about the review job.
        # 
        # *   Other configuration items of the review job. Only the ResourceType field is supported. This field is used to specify the type of media files. You can adjust review standards and rules based on the type of media files.
        # *   The value of ResourceType can contain only letters, digits, and underscores (_).
        # 
        # > *   You can specify a value for the ResourceType field based on the preceding limits. After you specify a value for the ResourceType field, you must [submit a ticket](https://yida.alibaba-inc.com/o/ticketapply). The value takes effect after Alibaba Cloud processes your ticket.
        # >*   If you want to change moderation policies and rules based on ResourceType, [submit a ticket](https://yida.alibaba-inc.com/o/ticketapply) to contact technical support.
        self.media_audit_configuration = media_audit_configuration
        # The ID of the image.
        # 
        # The unique ID of the image is returned after the image is uploaded to ApsaraVideo VOD.
        # 
        # This parameter is required.
        self.media_id = media_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the AI template. You can use one of the following methods to obtain the ID:
        # 
        # *   Obtain the value of TemplateId from the response to the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation that you call to create an AI template.
        # *   Obtain the value of TemplateId from the response to the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation that you call to create an AI template.
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

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

