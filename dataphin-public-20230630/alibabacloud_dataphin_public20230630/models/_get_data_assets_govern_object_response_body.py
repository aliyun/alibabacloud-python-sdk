# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataAssetsGovernObjectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        govern_object_info: main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The governance object details.
        self.govern_object_info = govern_object_info
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend response exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.govern_object_info:
            self.govern_object_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.govern_object_info is not None:
            result['GovernObjectInfo'] = self.govern_object_info.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GovernObjectInfo') is not None:
            temp_model = main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfo()
            self.govern_object_info = temp_model.from_map(m.get('GovernObjectInfo'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataAssetsGovernObjectResponseBodyGovernObjectInfo(DaraModel):
    def __init__(
        self,
        commit_time: str = None,
        govern_item_id: int = None,
        govern_object_id: int = None,
        is_rectify: bool = None,
        owners: List[main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoOwners] = None,
        problem: main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoProblem = None,
        properties: Dict[str, Any] = None,
        rectify_id: int = None,
        rectify_name: str = None,
        rectify_status: str = None,
        rectify_user: str = None,
        rectify_user_name: str = None,
        related_knowledge: List[main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoRelatedKnowledge] = None,
        status: str = None,
        submit_type: str = None,
        tenant_id: int = None,
    ):
        # The time when the governance object was reported.
        self.commit_time = commit_time
        # The governance object ID.
        self.govern_item_id = govern_item_id
        # The governance object ID.
        self.govern_object_id = govern_object_id
        # Indicates whether rectification is in progress.
        self.is_rectify = is_rectify
        # The list of owners.
        self.owners = owners
        # The governance issue object.
        self.problem = problem
        # The properties.
        self.properties = properties
        # The ID of the rectification.
        self.rectify_id = rectify_id
        # The name of the rectification.
        self.rectify_name = rectify_name
        # The rectification status.
        self.rectify_status = rectify_status
        # The ID of the user who performs the rectification.
        self.rectify_user = rectify_user
        # The display name of the rectification user.
        self.rectify_user_name = rectify_user_name
        # The related knowledge base.
        self.related_knowledge = related_knowledge
        # The status of the governance object.
        self.status = status
        # The submission method.
        self.submit_type = submit_type
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.owners:
            for v1 in self.owners:
                 if v1:
                    v1.validate()
        if self.problem:
            self.problem.validate()
        if self.related_knowledge:
            for v1 in self.related_knowledge:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_time is not None:
            result['CommitTime'] = self.commit_time

        if self.govern_item_id is not None:
            result['GovernItemId'] = self.govern_item_id

        if self.govern_object_id is not None:
            result['GovernObjectId'] = self.govern_object_id

        if self.is_rectify is not None:
            result['IsRectify'] = self.is_rectify

        result['Owners'] = []
        if self.owners is not None:
            for k1 in self.owners:
                result['Owners'].append(k1.to_map() if k1 else None)

        if self.problem is not None:
            result['Problem'] = self.problem.to_map()

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.rectify_id is not None:
            result['RectifyId'] = self.rectify_id

        if self.rectify_name is not None:
            result['RectifyName'] = self.rectify_name

        if self.rectify_status is not None:
            result['RectifyStatus'] = self.rectify_status

        if self.rectify_user is not None:
            result['RectifyUser'] = self.rectify_user

        if self.rectify_user_name is not None:
            result['RectifyUserName'] = self.rectify_user_name

        result['RelatedKnowledge'] = []
        if self.related_knowledge is not None:
            for k1 in self.related_knowledge:
                result['RelatedKnowledge'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_type is not None:
            result['SubmitType'] = self.submit_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitTime') is not None:
            self.commit_time = m.get('CommitTime')

        if m.get('GovernItemId') is not None:
            self.govern_item_id = m.get('GovernItemId')

        if m.get('GovernObjectId') is not None:
            self.govern_object_id = m.get('GovernObjectId')

        if m.get('IsRectify') is not None:
            self.is_rectify = m.get('IsRectify')

        self.owners = []
        if m.get('Owners') is not None:
            for k1 in m.get('Owners'):
                temp_model = main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoOwners()
                self.owners.append(temp_model.from_map(k1))

        if m.get('Problem') is not None:
            temp_model = main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoProblem()
            self.problem = temp_model.from_map(m.get('Problem'))

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RectifyId') is not None:
            self.rectify_id = m.get('RectifyId')

        if m.get('RectifyName') is not None:
            self.rectify_name = m.get('RectifyName')

        if m.get('RectifyStatus') is not None:
            self.rectify_status = m.get('RectifyStatus')

        if m.get('RectifyUser') is not None:
            self.rectify_user = m.get('RectifyUser')

        if m.get('RectifyUserName') is not None:
            self.rectify_user_name = m.get('RectifyUserName')

        self.related_knowledge = []
        if m.get('RelatedKnowledge') is not None:
            for k1 in m.get('RelatedKnowledge'):
                temp_model = main_models.GetDataAssetsGovernObjectResponseBodyGovernObjectInfoRelatedKnowledge()
                self.related_knowledge.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitType') is not None:
            self.submit_type = m.get('SubmitType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class GetDataAssetsGovernObjectResponseBodyGovernObjectInfoRelatedKnowledge(DaraModel):
    def __init__(
        self,
        cause: str = None,
        desc: str = None,
        knowledge_id: int = None,
        owner: str = None,
        owner_name: str = None,
        solution: str = None,
        title: str = None,
    ):
        # The cause of the issue.
        self.cause = cause
        # The description.
        self.desc = desc
        # The ID of the knowledge entry.
        self.knowledge_id = knowledge_id
        # The owner.
        self.owner = owner
        # The name of the owner.
        self.owner_name = owner_name
        # The Solutions.
        self.solution = solution
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetDataAssetsGovernObjectResponseBodyGovernObjectInfoProblem(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        parent_object_id: str = None,
        problem_contact_mail: str = None,
        problem_contact_other: str = None,
        problem_contact_phone: str = None,
        problem_desc: str = None,
        problem_submit_type: str = None,
        problem_submitter: str = None,
        problem_submitter_user_name: str = None,
        problem_types: List[str] = None,
    ):
        # The object ID.
        self.object_id = object_id
        # The ID of the parent object.
        self.parent_object_id = parent_object_id
        # The contact email for the governance issue.
        self.problem_contact_mail = problem_contact_mail
        # The other contact information for the governance issue.
        self.problem_contact_other = problem_contact_other
        # The contact phone number for the governance issue.
        self.problem_contact_phone = problem_contact_phone
        # The description of the governance issue.
        self.problem_desc = problem_desc
        # The submission method of the issue.
        self.problem_submit_type = problem_submit_type
        # The user who submitted the issue.
        self.problem_submitter = problem_submitter
        # The username of the user who submitted the issue.
        self.problem_submitter_user_name = problem_submitter_user_name
        # The types of the governance issue.
        self.problem_types = problem_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.parent_object_id is not None:
            result['ParentObjectId'] = self.parent_object_id

        if self.problem_contact_mail is not None:
            result['ProblemContactMail'] = self.problem_contact_mail

        if self.problem_contact_other is not None:
            result['ProblemContactOther'] = self.problem_contact_other

        if self.problem_contact_phone is not None:
            result['ProblemContactPhone'] = self.problem_contact_phone

        if self.problem_desc is not None:
            result['ProblemDesc'] = self.problem_desc

        if self.problem_submit_type is not None:
            result['ProblemSubmitType'] = self.problem_submit_type

        if self.problem_submitter is not None:
            result['ProblemSubmitter'] = self.problem_submitter

        if self.problem_submitter_user_name is not None:
            result['ProblemSubmitterUserName'] = self.problem_submitter_user_name

        if self.problem_types is not None:
            result['ProblemTypes'] = self.problem_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ParentObjectId') is not None:
            self.parent_object_id = m.get('ParentObjectId')

        if m.get('ProblemContactMail') is not None:
            self.problem_contact_mail = m.get('ProblemContactMail')

        if m.get('ProblemContactOther') is not None:
            self.problem_contact_other = m.get('ProblemContactOther')

        if m.get('ProblemContactPhone') is not None:
            self.problem_contact_phone = m.get('ProblemContactPhone')

        if m.get('ProblemDesc') is not None:
            self.problem_desc = m.get('ProblemDesc')

        if m.get('ProblemSubmitType') is not None:
            self.problem_submit_type = m.get('ProblemSubmitType')

        if m.get('ProblemSubmitter') is not None:
            self.problem_submitter = m.get('ProblemSubmitter')

        if m.get('ProblemSubmitterUserName') is not None:
            self.problem_submitter_user_name = m.get('ProblemSubmitterUserName')

        if m.get('ProblemTypes') is not None:
            self.problem_types = m.get('ProblemTypes')

        return self

class GetDataAssetsGovernObjectResponseBodyGovernObjectInfoOwners(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
    ):
        # The display name of the user.
        self.display_name = display_name
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

