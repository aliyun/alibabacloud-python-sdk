# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ContentPlanTopic(DaraModel):
    def __init__(
        self,
        article_conversation_id: str = None,
        article_id: str = None,
        article_status: str = None,
        diagnosis_references: List[str] = None,
        direction: str = None,
        fail_reason: str = None,
        plan_id: str = None,
        project_id: str = None,
        rationale: str = None,
        recommended_channels: List[str] = None,
        scheduled_at: str = None,
        skip_reason: str = None,
        status: str = None,
        title: str = None,
        topic_id: str = None,
        writing_direction: str = None,
    ):
        # The article generation session ID.
        self.article_conversation_id = article_conversation_id
        # The generated article ID.
        self.article_id = article_id
        # The status of the associated article. Valid values: DRAFT, PUBLISHED, and PUBLISH_FAILED. This parameter is empty if the article is not generated.
        self.article_status = article_status
        # The GEO diagnostic item references.
        self.diagnosis_references = diagnosis_references
        # The content direction.
        self.direction = direction
        # The reason for the execution failure.
        self.fail_reason = fail_reason
        # The content plan ID.
        self.plan_id = plan_id
        # The workspace ID. This refers to the GEO workspace for brand marketing, which is the appWorkspaceId.
        self.project_id = project_id
        # The rationale for topic selection.
        self.rationale = rationale
        # The recommended publishing channels.
        self.recommended_channels = recommended_channels
        # The scheduled publish date in the yyyy-MM-dd format.
        self.scheduled_at = scheduled_at
        # The reason for skipping.
        self.skip_reason = skip_reason
        # The topic status.
        self.status = status
        # The content title.
        self.title = title
        # The topic ID.
        self.topic_id = topic_id
        # The writing direction, which only describes the structure and perspective.
        self.writing_direction = writing_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_conversation_id is not None:
            result['ArticleConversationId'] = self.article_conversation_id

        if self.article_id is not None:
            result['ArticleId'] = self.article_id

        if self.article_status is not None:
            result['ArticleStatus'] = self.article_status

        if self.diagnosis_references is not None:
            result['DiagnosisReferences'] = self.diagnosis_references

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rationale is not None:
            result['Rationale'] = self.rationale

        if self.recommended_channels is not None:
            result['RecommendedChannels'] = self.recommended_channels

        if self.scheduled_at is not None:
            result['ScheduledAt'] = self.scheduled_at

        if self.skip_reason is not None:
            result['SkipReason'] = self.skip_reason

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.writing_direction is not None:
            result['WritingDirection'] = self.writing_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArticleConversationId') is not None:
            self.article_conversation_id = m.get('ArticleConversationId')

        if m.get('ArticleId') is not None:
            self.article_id = m.get('ArticleId')

        if m.get('ArticleStatus') is not None:
            self.article_status = m.get('ArticleStatus')

        if m.get('DiagnosisReferences') is not None:
            self.diagnosis_references = m.get('DiagnosisReferences')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Rationale') is not None:
            self.rationale = m.get('Rationale')

        if m.get('RecommendedChannels') is not None:
            self.recommended_channels = m.get('RecommendedChannels')

        if m.get('ScheduledAt') is not None:
            self.scheduled_at = m.get('ScheduledAt')

        if m.get('SkipReason') is not None:
            self.skip_reason = m.get('SkipReason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('WritingDirection') is not None:
            self.writing_direction = m.get('WritingDirection')

        return self

