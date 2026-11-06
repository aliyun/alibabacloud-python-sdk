# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetCodeReviewResponseBody(DaraModel):
    def __init__(
        self,
        code_review: main_models.GetCodeReviewResponseBodyCodeReview = None,
        request_id: str = None,
    ):
        # The code review metadata.
        self.code_review = code_review
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.code_review:
            self.code_review.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_review is not None:
            result['CodeReview'] = self.code_review.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeReview') is not None:
            temp_model = main_models.GetCodeReviewResponseBodyCodeReview()
            self.code_review = temp_model.from_map(m.get('CodeReview'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCodeReviewResponseBodyCodeReview(DaraModel):
    def __init__(
        self,
        command: str = None,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        final_reviewer: str = None,
        id: str = None,
        modify_time: int = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        project_id: int = None,
        region_id: str = None,
        review_time: int = None,
        reviewers: List[str] = None,
        status: str = None,
    ):
        # The node command of the root object.
        self.command = command
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The account ID of the actual submitter.
        self.creator = creator
        # The review description provided at creation.
        self.description = description
        # The account ID of the final approver. This field is empty if no approval decision has been made.
        self.final_reviewer = final_reviewer
        # The unique identifier of the review.
        self.id = id
        # The update time. The value is a UNIX timestamp in milliseconds.
        self.modify_time = modify_time
        # The ID of the root review object.
        self.object_id = object_id
        # The name of the root review object.
        self.object_name = object_name
        # The object type of the root object.
        self.object_type = object_type
        # The workspace ID.
        self.project_id = project_id
        # The region ID.
        self.region_id = region_id
        # The approval time. This field is empty if no approval decision has been made.
        self.review_time = review_time
        # The account IDs of the designated reviewers.
        self.reviewers = reviewers
        # The review status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.final_reviewer is not None:
            result['FinalReviewer'] = self.final_reviewer

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.review_time is not None:
            result['ReviewTime'] = self.review_time

        if self.reviewers is not None:
            result['Reviewers'] = self.reviewers

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FinalReviewer') is not None:
            self.final_reviewer = m.get('FinalReviewer')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReviewTime') is not None:
            self.review_time = m.get('ReviewTime')

        if m.get('Reviewers') is not None:
            self.reviewers = m.get('Reviewers')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

