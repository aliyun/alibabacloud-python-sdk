# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetNodeDetailResponseBody(DaraModel):
    def __init__(
        self,
        agent_work_process: main_models.GetNodeDetailResponseBodyAgentWorkProcess = None,
        artifacts: List[main_models.GetNodeDetailResponseBodyArtifacts] = None,
        attempt_seq: int = None,
        code: str = None,
        conversation_id: str = None,
        conversation_writable: bool = None,
        handler: str = None,
        message: str = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        resume_pending: bool = None,
        run_log: List[main_models.GetNodeDetailResponseBodyRunLog] = None,
        state_version: int = None,
        status: str = None,
        todo_ids: List[str] = None,
        turn_seq: int = None,
        wait_type: str = None,
    ):
        # The actual work process grouped by thoughts, skills, tools, replies, and artifacts.
        self.agent_work_process = agent_work_process
        # The artifacts: saved node work records and artifacts.
        self.artifacts = artifacts
        # The sequence number of the node execution attempt.
        self.attempt_seq = attempt_seq
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The node conversation ID. This parameter is empty if no conversation is created.
        self.conversation_id = conversation_id
        # Indicates whether the current node conversation can continue to receive input.
        self.conversation_writable = conversation_writable
        # The display name of the node owner. This parameter is empty if the owner is unknown.
        self.handler = handler
        # The error description.
        self.message = message
        # The node key.
        self.node_id = node_id
        # The display name of the node, which shares the same source as the node list.
        self.node_name = node_name
        # The node type. The actual enum value is returned.
        self.node_type = node_type
        # The request tracking ID.
        self.request_id = request_id
        # The node result summary, excluding inline content.
        self.result = result
        # Indicates whether there are pending follow-up turns to be dispatched.
        self.resume_pending = resume_pending
        # The run log: saved node work records and artifacts.
        self.run_log = run_log
        # stateVersion
        self.state_version = state_version
        # The node running status. The actual enum value is returned.
        self.status = status
        # The list of to-do IDs associated with the current node.
        self.todo_ids = todo_ids
        # The sequence number of the conversation turn in the current attempt.
        self.turn_seq = turn_seq
        # The reason why the node is waiting. This parameter is empty if the node is not waiting.
        self.wait_type = wait_type

    def validate(self):
        if self.agent_work_process:
            self.agent_work_process.validate()
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()
        if self.run_log:
            for v1 in self.run_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_work_process is not None:
            result['agentWorkProcess'] = self.agent_work_process.to_map()

        result['artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['artifacts'].append(k1.to_map() if k1 else None)

        if self.attempt_seq is not None:
            result['attemptSeq'] = self.attempt_seq

        if self.code is not None:
            result['code'] = self.code

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.conversation_writable is not None:
            result['conversationWritable'] = self.conversation_writable

        if self.handler is not None:
            result['handler'] = self.handler

        if self.message is not None:
            result['message'] = self.message

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result

        if self.resume_pending is not None:
            result['resumePending'] = self.resume_pending

        result['runLog'] = []
        if self.run_log is not None:
            for k1 in self.run_log:
                result['runLog'].append(k1.to_map() if k1 else None)

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        if self.status is not None:
            result['status'] = self.status

        if self.todo_ids is not None:
            result['todoIds'] = self.todo_ids

        if self.turn_seq is not None:
            result['turnSeq'] = self.turn_seq

        if self.wait_type is not None:
            result['waitType'] = self.wait_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentWorkProcess') is not None:
            temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcess()
            self.agent_work_process = temp_model.from_map(m.get('agentWorkProcess'))

        self.artifacts = []
        if m.get('artifacts') is not None:
            for k1 in m.get('artifacts'):
                temp_model = main_models.GetNodeDetailResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('attemptSeq') is not None:
            self.attempt_seq = m.get('attemptSeq')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('conversationWritable') is not None:
            self.conversation_writable = m.get('conversationWritable')

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('resumePending') is not None:
            self.resume_pending = m.get('resumePending')

        self.run_log = []
        if m.get('runLog') is not None:
            for k1 in m.get('runLog'):
                temp_model = main_models.GetNodeDetailResponseBodyRunLog()
                self.run_log.append(temp_model.from_map(k1))

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('todoIds') is not None:
            self.todo_ids = m.get('todoIds')

        if m.get('turnSeq') is not None:
            self.turn_seq = m.get('turnSeq')

        if m.get('waitType') is not None:
            self.wait_type = m.get('waitType')

        return self

class GetNodeDetailResponseBodyRunLog(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, or ARTIFACT.
        self.action = action
        # The saved original record content. Tool invocation and artifact metadata are JSON strings.
        self.detail = detail
        # The time taken for this work record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the parent node, not the conversation ID.
        self.node_id = node_id
        # The time when the event is recorded, in ISO-8601 format. This is an empty string if the source record has no time.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetNodeDetailResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_key: str = None,
        ref: Dict[str, str] = None,
        summary: str = None,
        title: str = None,
        type: str = None,
    ):
        # The registered artifact ID. This parameter may be empty for artifacts derived only from the result summary.
        self.artifact_id = artifact_id
        # The unique key of the artifact in the node result.
        self.artifact_key = artifact_key
        # The stable reference of the artifact, including kind, id, and url. The URL of a registered artifact is a re-authentication entry point and can be empty.
        self.ref = ref
        # The artifact summary, excluding inline content.
        self.summary = summary
        # The display title of the artifact.
        self.title = title
        # The artifact type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.artifact_key is not None:
            result['artifactKey'] = self.artifact_key

        if self.ref is not None:
            result['ref'] = self.ref

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('artifactKey') is not None:
            self.artifact_key = m.get('artifactKey')

        if m.get('ref') is not None:
            self.ref = m.get('ref')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetNodeDetailResponseBodyAgentWorkProcess(DaraModel):
    def __init__(
        self,
        artifacts: List[main_models.GetNodeDetailResponseBodyAgentWorkProcessArtifacts] = None,
        replies: List[main_models.GetNodeDetailResponseBodyAgentWorkProcessReplies] = None,
        skill_calls: List[main_models.GetNodeDetailResponseBodyAgentWorkProcessSkillCalls] = None,
        thoughts: List[main_models.GetNodeDetailResponseBodyAgentWorkProcessThoughts] = None,
        tool_calls: List[main_models.GetNodeDetailResponseBodyAgentWorkProcessToolCalls] = None,
    ):
        # The artifacts: saved node work records and artifacts.
        self.artifacts = artifacts
        # The replies: saved node work records and artifacts.
        self.replies = replies
        # The skill calls: saved node work records and artifacts.
        self.skill_calls = skill_calls
        # The thoughts: saved node work records and artifacts.
        self.thoughts = thoughts
        # The tool calls: saved node work records and artifacts.
        self.tool_calls = tool_calls

    def validate(self):
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()
        if self.replies:
            for v1 in self.replies:
                 if v1:
                    v1.validate()
        if self.skill_calls:
            for v1 in self.skill_calls:
                 if v1:
                    v1.validate()
        if self.thoughts:
            for v1 in self.thoughts:
                 if v1:
                    v1.validate()
        if self.tool_calls:
            for v1 in self.tool_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['artifacts'].append(k1.to_map() if k1 else None)

        result['replies'] = []
        if self.replies is not None:
            for k1 in self.replies:
                result['replies'].append(k1.to_map() if k1 else None)

        result['skillCalls'] = []
        if self.skill_calls is not None:
            for k1 in self.skill_calls:
                result['skillCalls'].append(k1.to_map() if k1 else None)

        result['thoughts'] = []
        if self.thoughts is not None:
            for k1 in self.thoughts:
                result['thoughts'].append(k1.to_map() if k1 else None)

        result['toolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['toolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.artifacts = []
        if m.get('artifacts') is not None:
            for k1 in m.get('artifacts'):
                temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcessArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        self.replies = []
        if m.get('replies') is not None:
            for k1 in m.get('replies'):
                temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcessReplies()
                self.replies.append(temp_model.from_map(k1))

        self.skill_calls = []
        if m.get('skillCalls') is not None:
            for k1 in m.get('skillCalls'):
                temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcessSkillCalls()
                self.skill_calls.append(temp_model.from_map(k1))

        self.thoughts = []
        if m.get('thoughts') is not None:
            for k1 in m.get('thoughts'):
                temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcessThoughts()
                self.thoughts.append(temp_model.from_map(k1))

        self.tool_calls = []
        if m.get('toolCalls') is not None:
            for k1 in m.get('toolCalls'):
                temp_model = main_models.GetNodeDetailResponseBodyAgentWorkProcessToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class GetNodeDetailResponseBodyAgentWorkProcessToolCalls(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, or ARTIFACT.
        self.action = action
        # The saved original record content. Tool invocation and artifact metadata are JSON strings.
        self.detail = detail
        # The time taken for this work record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the parent node, not the conversation ID.
        self.node_id = node_id
        # The time when the event is recorded, in ISO-8601 format. This is an empty string if the source record has no time.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetNodeDetailResponseBodyAgentWorkProcessThoughts(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, or ARTIFACT.
        self.action = action
        # The saved original record content. Tool invocation and artifact metadata are JSON strings.
        self.detail = detail
        # The time taken for this work record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the parent node, not the conversation ID.
        self.node_id = node_id
        # The time when the event is recorded, in ISO-8601 format. This is an empty string if the source record has no time.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetNodeDetailResponseBodyAgentWorkProcessSkillCalls(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, or ARTIFACT.
        self.action = action
        # The saved original record content. Tool invocation and artifact metadata are JSON strings.
        self.detail = detail
        # The time taken for this work record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the parent node, not the conversation ID.
        self.node_id = node_id
        # The time when the event is recorded, in ISO-8601 format. This is an empty string if the source record has no time.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetNodeDetailResponseBodyAgentWorkProcessReplies(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # The record type. Valid values: THINK, REPLY, TOOL_CALL, SKILL_CALL, or ARTIFACT.
        self.action = action
        # The saved original record content. Tool invocation and artifact metadata are JSON strings.
        self.detail = detail
        # The time taken for this work record, in milliseconds. The value is 0 for artifact records.
        self.duration = duration
        # The key of the parent node, not the conversation ID.
        self.node_id = node_id
        # The time when the event is recorded, in ISO-8601 format. This is an empty string if the source record has no time.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class GetNodeDetailResponseBodyAgentWorkProcessArtifacts(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        artifact_key: str = None,
        ref: Dict[str, str] = None,
        summary: str = None,
        title: str = None,
        type: str = None,
    ):
        # The registered artifact ID. This parameter may be empty for artifacts derived only from the result summary.
        self.artifact_id = artifact_id
        # The unique key of the artifact in the node result.
        self.artifact_key = artifact_key
        # The stable reference of the artifact, including kind, id, and url. The URL of a registered artifact is a re-authentication entry point and can be empty.
        self.ref = ref
        # The artifact summary, excluding inline content.
        self.summary = summary
        # The display title of the artifact.
        self.title = title
        # The artifact type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.artifact_key is not None:
            result['artifactKey'] = self.artifact_key

        if self.ref is not None:
            result['ref'] = self.ref

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('artifactKey') is not None:
            self.artifact_key = m.get('artifactKey')

        if m.get('ref') is not None:
            self.ref = m.get('ref')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

