# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetRepoBuildRecordResponseBody(DaraModel):
    def __init__(
        self,
        build_record_id: str = None,
        code: str = None,
        end_time: int = None,
        image: main_models.GetRepoBuildRecordResponseBodyImage = None,
        is_success: bool = None,
        request_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The return value.
        self.code = code
        # The time when the image building was completed.
        self.end_time = end_time
        # The information about the image.
        self.image = image
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The time when the image building started.
        self.start_time = start_time
        # The status of the instance.
        self.status = status

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id

        if self.code is not None:
            result['Code'] = self.code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Image') is not None:
            temp_model = main_models.GetRepoBuildRecordResponseBodyImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetRepoBuildRecordResponseBodyImage(DaraModel):
    def __init__(
        self,
        image_tag: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        # The tag of the image.
        self.image_tag = image_tag
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace to which the image repository belongs.
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        return self

