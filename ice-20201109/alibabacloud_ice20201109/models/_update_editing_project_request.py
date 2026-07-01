# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEditingProjectRequest(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        clips_param: str = None,
        cover_url: str = None,
        description: str = None,
        project_id: str = None,
        template_id: str = None,
        timeline: str = None,
        title: str = None,
    ):
        # The business status of the project. You can typically ignore this parameter for standard cloud editing projects. Use this parameter to modify the project\\"s reservation status:
        # 
        # - `Reserving`: The project is being reserved.
        # 
        # - `ReservationCanceled`: The reservation for the project is canceled.
        self.business_status = business_status
        # The clip parameters for the template, in JSON format. This parameter is required if you specify `TemplateId`.<props="china"> For more information about the format, see [Create and use a standard template](https://help.aliyun.com/document_detail/328557.html) and [Create and use an advanced template](https://help.aliyun.com/document_detail/291418.html).
        self.clips_param = clips_param
        # The project cover.
        self.cover_url = cover_url
        # The project description.
        self.description = description
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The template ID. Use this parameter to quickly build a timeline.>Notice: You can specify only one of `ProjectId`, `Timeline`, and `TemplateId`. If you specify `TemplateId`, `ClipsParam` is required.
        self.template_id = template_id
        # The project timeline, in JSON format.
        self.timeline = timeline
        # The project title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

