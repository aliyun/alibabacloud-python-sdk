# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class DeleteWorkflowTemplateVersionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        effective_version: str = None,
        items: List[main_models.DeleteWorkflowTemplateVersionResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        template_id: str = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The current active version number. An empty value indicates that only a draft exists.
        self.effective_version = effective_version
        # All remaining versions after deletion, sorted in descending order by version number.
        self.items = items
        # The error message.
        self.message = message
        # The request tracking ID.
        self.request_id = request_id
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.effective_version is not None:
            result['effectiveVersion'] = self.effective_version

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('effectiveVersion') is not None:
            self.effective_version = m.get('effectiveVersion')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DeleteWorkflowTemplateVersionResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

class DeleteWorkflowTemplateVersionResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_by_user_id: int = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        gmt_submitted: str = None,
        is_effective: bool = None,
        name: str = None,
        source_version: str = None,
        status: str = None,
        step_count: int = None,
        submitted_by_user_id: int = None,
        updated_by_user_id: int = None,
        version: str = None,
        version_description: str = None,
    ):
        # The ID of the user who created the version.
        self.created_by_user_id = created_by_user_id
        # The description of the template for this version. This can be used for display when version v1 has no version description.
        self.description = description
        # The time when the version was created. The time is in the ISO 8601 format.
        self.gmt_create = gmt_create
        # The time when the version was modified. The time is in the ISO 8601 format.
        self.gmt_modified = gmt_modified
        # The time when the version was submitted. The time is in the ISO 8601 format. This is empty for a draft.
        self.gmt_submitted = gmt_submitted
        # Indicates whether the version is the only current active version.
        self.is_effective = is_effective
        # The name of the template for this version.
        self.name = name
        # The submitted version number on which this version is based. This is empty for a newly created v1 version. Saving or submitting a draft retains the original source version.
        self.source_version = source_version
        # The version status. Valid values: DRAFT (draft) and SUBMITTED (submitted).
        self.status = status
        # The number of steps in this version.
        self.step_count = step_count
        # The ID of the user who submitted the version. This is empty for a draft.
        self.submitted_by_user_id = submitted_by_user_id
        # The ID of the user who last modified the version.
        self.updated_by_user_id = updated_by_user_id
        # The version number.
        self.version = version
        # The persisted version change description. An empty value indicates that no description is provided.
        self.version_description = version_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_by_user_id is not None:
            result['createdByUserId'] = self.created_by_user_id

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.gmt_submitted is not None:
            result['gmtSubmitted'] = self.gmt_submitted

        if self.is_effective is not None:
            result['isEffective'] = self.is_effective

        if self.name is not None:
            result['name'] = self.name

        if self.source_version is not None:
            result['sourceVersion'] = self.source_version

        if self.status is not None:
            result['status'] = self.status

        if self.step_count is not None:
            result['stepCount'] = self.step_count

        if self.submitted_by_user_id is not None:
            result['submittedByUserId'] = self.submitted_by_user_id

        if self.updated_by_user_id is not None:
            result['updatedByUserId'] = self.updated_by_user_id

        if self.version is not None:
            result['version'] = self.version

        if self.version_description is not None:
            result['versionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdByUserId') is not None:
            self.created_by_user_id = m.get('createdByUserId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('gmtSubmitted') is not None:
            self.gmt_submitted = m.get('gmtSubmitted')

        if m.get('isEffective') is not None:
            self.is_effective = m.get('isEffective')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceVersion') is not None:
            self.source_version = m.get('sourceVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('stepCount') is not None:
            self.step_count = m.get('stepCount')

        if m.get('submittedByUserId') is not None:
            self.submitted_by_user_id = m.get('submittedByUserId')

        if m.get('updatedByUserId') is not None:
            self.updated_by_user_id = m.get('updatedByUserId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionDescription') is not None:
            self.version_description = m.get('versionDescription')

        return self

