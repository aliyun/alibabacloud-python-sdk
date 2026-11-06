# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCodeReviewsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCodeReviewsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCodeReviewsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCodeReviewsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        code_reviews: List[main_models.ListCodeReviewsResponseBodyPagingInfoCodeReviews] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of code reviews.
        self.code_reviews = code_reviews
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.code_reviews:
            for v1 in self.code_reviews:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeReviews'] = []
        if self.code_reviews is not None:
            for k1 in self.code_reviews:
                result['CodeReviews'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_reviews = []
        if m.get('CodeReviews') is not None:
            for k1 in m.get('CodeReviews'):
                temp_model = main_models.ListCodeReviewsResponseBodyPagingInfoCodeReviews()
                self.code_reviews.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCodeReviewsResponseBodyPagingInfoCodeReviews(DaraModel):
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
        # The review description provided upon creation.
        self.description = description
        # The account ID of the final approver. This field is empty if no approval decision has been made.
        self.final_reviewer = final_reviewer
        # The unique ID of the review.
        self.id = id
        # The update time. The value is a UNIX timestamp in milliseconds.
        self.modify_time = modify_time
        # The ID of the root review object.
        self.object_id = object_id
        # The name of the root review object.
        self.object_name = object_name
        # The root object type.
        self.object_type = object_type
        # The workspace ID.
        self.project_id = project_id
        # The region ID.
        self.region_id = region_id
        # The approval time. This field is empty if no approval decision has been made.
        self.review_time = review_time
        # The list of account IDs of the specified reviewers.
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

