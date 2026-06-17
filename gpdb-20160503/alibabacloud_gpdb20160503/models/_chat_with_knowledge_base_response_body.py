# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ChatWithKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        chat_completion: main_models.ChatWithKnowledgeBaseResponseBodyChatCompletion = None,
        message: str = None,
        multi_collection_recall_result: main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResult = None,
        request_id: str = None,
        status: str = None,
    ):
        # The response from the large language model.
        self.chat_completion = chat_completion
        # A message that provides details about the status of the operation.
        self.message = message
        # The recall results from multiple knowledge bases.
        self.multi_collection_recall_result = multi_collection_recall_result
        # The request ID.
        self.request_id = request_id
        # The final status of the request. Valid values:
        # 
        # - `success`: The request was successful.
        # 
        # - `fail`: The request failed.
        self.status = status

    def validate(self):
        if self.chat_completion:
            self.chat_completion.validate()
        if self.multi_collection_recall_result:
            self.multi_collection_recall_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_completion is not None:
            result['ChatCompletion'] = self.chat_completion.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.multi_collection_recall_result is not None:
            result['MultiCollectionRecallResult'] = self.multi_collection_recall_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatCompletion') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletion()
            self.chat_completion = temp_model.from_map(m.get('ChatCompletion'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MultiCollectionRecallResult') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResult()
            self.multi_collection_recall_result = temp_model.from_map(m.get('MultiCollectionRecallResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResult(DaraModel):
    def __init__(
        self,
        entities: List[str] = None,
        matches: List[main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultMatches] = None,
        relations: List[str] = None,
        request_id: str = None,
        status: str = None,
        tokens: int = None,
        usage: main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultUsage = None,
    ):
        # A list of identified entity types.
        self.entities = entities
        # The recalled items.
        self.matches = matches
        # The relationship edges.
        self.relations = relations
        # The request ID.
        self.request_id = request_id
        # The status of the recall operation. Valid values:
        # 
        # - `success`: The recall was successful.
        # 
        # - `fail`: The recall failed.
        self.status = status
        # The number of tokens consumed by the recall process.
        self.tokens = tokens
        # Usage statistics for the recall, such as the number of tokens for vectorization.
        self.usage = usage

    def validate(self):
        if self.matches:
            for v1 in self.matches:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entities is not None:
            result['Entities'] = self.entities

        result['Matches'] = []
        if self.matches is not None:
            for k1 in self.matches:
                result['Matches'].append(k1.to_map() if k1 else None)

        if self.relations is not None:
            result['Relations'] = self.relations

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entities') is not None:
            self.entities = m.get('Entities')

        self.matches = []
        if m.get('Matches') is not None:
            for k1 in m.get('Matches'):
                temp_model = main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultMatches()
                self.matches.append(temp_model.from_map(k1))

        if m.get('Relations') is not None:
            self.relations = m.get('Relations')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        if m.get('Usage') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultUsage(DaraModel):
    def __init__(
        self,
        embedding_tokens: int = None,
    ):
        # The number of tokens used for vectorization.
        # 
        # > A token is the smallest unit of text. A token can be a word, a phrase, a punctuation mark, or a character.
        self.embedding_tokens = embedding_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.embedding_tokens is not None:
            result['EmbeddingTokens'] = self.embedding_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmbeddingTokens') is not None:
            self.embedding_tokens = m.get('EmbeddingTokens')

        return self

class ChatWithKnowledgeBaseResponseBodyMultiCollectionRecallResultMatches(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        file_url: str = None,
        id: str = None,
        loader_metadata: Any = None,
        metadata: Dict[str, Any] = None,
        rerank_score: float = None,
        retrieval_source: int = None,
        score: float = None,
        vector: List[float] = None,
    ):
        # The document content.
        self.content = content
        # The file name.
        self.file_name = file_name
        # The public URL of the file. By default, the URL is valid for 2 hours.
        # 
        # You can specify a custom validity period by using the `UrlExpiration` request parameter.
        self.file_url = file_url
        # The unique ID of the vector.
        self.id = id
        # The metadata generated when the document was loaded.
        self.loader_metadata = loader_metadata
        # The metadata.
        self.metadata = metadata
        # The reranking score.
        self.rerank_score = rerank_score
        # The retrieval source. Valid values: `1` for vector retrieval, `2` for full-text search, and `3` for two-channel recall.
        self.retrieval_source = retrieval_source
        # The similarity score. The score is based on the algorithm `(l2/ip/cosine)` specified when the index was created.
        self.score = score
        # The vector data.
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.id is not None:
            result['Id'] = self.id

        if self.loader_metadata is not None:
            result['LoaderMetadata'] = self.loader_metadata

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.rerank_score is not None:
            result['RerankScore'] = self.rerank_score

        if self.retrieval_source is not None:
            result['RetrievalSource'] = self.retrieval_source

        if self.score is not None:
            result['Score'] = self.score

        if self.vector is not None:
            result['Vector'] = self.vector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LoaderMetadata') is not None:
            self.loader_metadata = m.get('LoaderMetadata')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RerankScore') is not None:
            self.rerank_score = m.get('RerankScore')

        if m.get('RetrievalSource') is not None:
            self.retrieval_source = m.get('RetrievalSource')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Vector') is not None:
            self.vector = m.get('Vector')

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletion(DaraModel):
    def __init__(
        self,
        choices: List[main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoices] = None,
        created: int = None,
        id: str = None,
        model: str = None,
        usage: main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionUsage = None,
    ):
        # A list of chat completion choices.
        self.choices = choices
        # The creation time of the response, as a Unix timestamp.
        self.created = created
        # The response ID.
        self.id = id
        # The model that generated the response.
        self.model = model
        # Token usage statistics for the chat completion.
        self.usage = usage

    def validate(self):
        if self.choices:
            for v1 in self.choices:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Choices'] = []
        if self.choices is not None:
            for k1 in self.choices:
                result['Choices'].append(k1.to_map() if k1 else None)

        if self.created is not None:
            result['Created'] = self.created

        if self.id is not None:
            result['Id'] = self.id

        if self.model is not None:
            result['Model'] = self.model

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('Choices') is not None:
            for k1 in m.get('Choices'):
                temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoices()
                self.choices.append(temp_model.from_map(k1))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Usage') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionUsage(DaraModel):
    def __init__(
        self,
        completion_tokens: int = None,
        prompt_tokens: int = None,
        prompt_tokens_details: main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionUsagePromptTokensDetails = None,
        total_tokens: int = None,
    ):
        # The number of tokens in the generated response.
        self.completion_tokens = completion_tokens
        # The number of tokens in the input prompt.
        self.prompt_tokens = prompt_tokens
        # Details of the prompt tokens.
        self.prompt_tokens_details = prompt_tokens_details
        # The total number of tokens used in the request (prompt tokens + completion tokens).
        self.total_tokens = total_tokens

    def validate(self):
        if self.prompt_tokens_details:
            self.prompt_tokens_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.prompt_tokens_details is not None:
            result['PromptTokensDetails'] = self.prompt_tokens_details.to_map()

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('PromptTokensDetails') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionUsagePromptTokensDetails()
            self.prompt_tokens_details = temp_model.from_map(m.get('PromptTokensDetails'))

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionUsagePromptTokensDetails(DaraModel):
    def __init__(
        self,
        cached_tokens: int = None,
    ):
        # The number of prompt tokens that resulted in a cache hit.
        self.cached_tokens = cached_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cached_tokens is not None:
            result['CachedTokens'] = self.cached_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CachedTokens') is not None:
            self.cached_tokens = m.get('CachedTokens')

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionChoices(DaraModel):
    def __init__(
        self,
        finish_reason: str = None,
        index: int = None,
        message: main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessage = None,
    ):
        # The reason the model stopped generating tokens.
        self.finish_reason = finish_reason
        # The index of this choice in the `Choices` array.
        self.index = index
        # The message generated by the large language model.
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason

        if self.index is not None:
            result['Index'] = self.index

        if self.message is not None:
            result['Message'] = self.message.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Message') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessage()
            self.message = temp_model.from_map(m.get('Message'))

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        reasoning_content: str = None,
        role: str = None,
        tool_calls: List[main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCalls] = None,
    ):
        # The content of the message.
        self.content = content
        # The model\\"s reasoning process.
        self.reasoning_content = reasoning_content
        # The role of the message:
        # 
        # - `system`
        # 
        # - `user`
        # 
        # - `assistant`
        self.role = role
        # A list of tool calls generated by the model.
        self.tool_calls = tool_calls

    def validate(self):
        if self.tool_calls:
            for v1 in self.tool_calls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.reasoning_content is not None:
            result['ReasoningContent'] = self.reasoning_content

        if self.role is not None:
            result['Role'] = self.role

        result['ToolCalls'] = []
        if self.tool_calls is not None:
            for k1 in self.tool_calls:
                result['ToolCalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ReasoningContent') is not None:
            self.reasoning_content = m.get('ReasoningContent')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        self.tool_calls = []
        if m.get('ToolCalls') is not None:
            for k1 in m.get('ToolCalls'):
                temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCalls()
                self.tool_calls.append(temp_model.from_map(k1))

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCalls(DaraModel):
    def __init__(
        self,
        function: main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCallsFunction = None,
        id: str = None,
        index: int = None,
    ):
        # The function that the model wants to call.
        self.function = function
        # The ID of the tool call.
        self.id = id
        # The index of the tool call.
        self.index = index

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.index is not None:
            result['Index'] = self.index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = main_models.ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCallsFunction()
            self.function = temp_model.from_map(m.get('Function'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        return self

class ChatWithKnowledgeBaseResponseBodyChatCompletionChoicesMessageToolCallsFunction(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        name: str = None,
    ):
        # The arguments to pass to the function.
        self.arguments = arguments
        # The name of the function to call.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['Arguments'] = self.arguments

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

