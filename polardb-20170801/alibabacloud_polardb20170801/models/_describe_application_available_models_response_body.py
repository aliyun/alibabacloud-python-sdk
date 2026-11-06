# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationAvailableModelsResponseBody(DaraModel):
    def __init__(
        self,
        asr_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyAsrModels] = None,
        default_embedding_model: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultEmbeddingModel = None,
        default_graph_llmmodel: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultGraphLLMModel = None,
        default_llmmodel: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultLLMModel = None,
        default_memory_type: str = None,
        default_rerank_model: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultRerankModel = None,
        default_vlmodel: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVLModel = None,
        default_visual_embedder_model: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVisualEmbedderModel = None,
        default_visual_llm_model: main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVisualLlmModel = None,
        embedding_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyEmbeddingModels] = None,
        graph_llm_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyGraphLlmModels] = None,
        llm_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyLlmModels] = None,
        memory_types: List[str] = None,
        multimodal_supported: bool = None,
        request_id: str = None,
        rerank_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyRerankModels] = None,
        vlmodels: List[main_models.DescribeApplicationAvailableModelsResponseBodyVLModels] = None,
        visual_embedder_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyVisualEmbedderModels] = None,
        visual_llm_models: List[main_models.DescribeApplicationAvailableModelsResponseBodyVisualLlmModels] = None,
    ):
        # The list of speech recognition models.
        self.asr_models = asr_models
        # The default text embedding model.
        self.default_embedding_model = default_embedding_model
        # The default graph large language model.
        self.default_graph_llmmodel = default_graph_llmmodel
        # The default large language model.
        self.default_llmmodel = default_llmmodel
        # The default memory type.
        self.default_memory_type = default_memory_type
        # The default reranking model.
        self.default_rerank_model = default_rerank_model
        # The default vision-language model.
        self.default_vlmodel = default_vlmodel
        # The default VisualEmbedder model.
        self.default_visual_embedder_model = default_visual_embedder_model
        # The default VisualLLM model.
        self.default_visual_llm_model = default_visual_llm_model
        # The list of available text embedding models.
        self.embedding_models = embedding_models
        # The list of available graph large language models.
        self.graph_llm_models = graph_llm_models
        # The list of available large language models.
        self.llm_models = llm_models
        # The available memory types.
        self.memory_types = memory_types
        # Indicates whether the current account supports Mem0 multimodal.
        self.multimodal_supported = multimodal_supported
        # The request ID.
        self.request_id = request_id
        # The list of available reranking models.
        self.rerank_models = rerank_models
        # The list of available vision-language models.
        self.vlmodels = vlmodels
        # The list of available VisualEmbedder models.
        self.visual_embedder_models = visual_embedder_models
        # The list of available VisualLLM models.
        self.visual_llm_models = visual_llm_models

    def validate(self):
        if self.asr_models:
            for v1 in self.asr_models:
                 if v1:
                    v1.validate()
        if self.default_embedding_model:
            self.default_embedding_model.validate()
        if self.default_graph_llmmodel:
            self.default_graph_llmmodel.validate()
        if self.default_llmmodel:
            self.default_llmmodel.validate()
        if self.default_rerank_model:
            self.default_rerank_model.validate()
        if self.default_vlmodel:
            self.default_vlmodel.validate()
        if self.default_visual_embedder_model:
            self.default_visual_embedder_model.validate()
        if self.default_visual_llm_model:
            self.default_visual_llm_model.validate()
        if self.embedding_models:
            for v1 in self.embedding_models:
                 if v1:
                    v1.validate()
        if self.graph_llm_models:
            for v1 in self.graph_llm_models:
                 if v1:
                    v1.validate()
        if self.llm_models:
            for v1 in self.llm_models:
                 if v1:
                    v1.validate()
        if self.rerank_models:
            for v1 in self.rerank_models:
                 if v1:
                    v1.validate()
        if self.vlmodels:
            for v1 in self.vlmodels:
                 if v1:
                    v1.validate()
        if self.visual_embedder_models:
            for v1 in self.visual_embedder_models:
                 if v1:
                    v1.validate()
        if self.visual_llm_models:
            for v1 in self.visual_llm_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AsrModels'] = []
        if self.asr_models is not None:
            for k1 in self.asr_models:
                result['AsrModels'].append(k1.to_map() if k1 else None)

        if self.default_embedding_model is not None:
            result['DefaultEmbeddingModel'] = self.default_embedding_model.to_map()

        if self.default_graph_llmmodel is not None:
            result['DefaultGraphLLMModel'] = self.default_graph_llmmodel.to_map()

        if self.default_llmmodel is not None:
            result['DefaultLLMModel'] = self.default_llmmodel.to_map()

        if self.default_memory_type is not None:
            result['DefaultMemoryType'] = self.default_memory_type

        if self.default_rerank_model is not None:
            result['DefaultRerankModel'] = self.default_rerank_model.to_map()

        if self.default_vlmodel is not None:
            result['DefaultVLModel'] = self.default_vlmodel.to_map()

        if self.default_visual_embedder_model is not None:
            result['DefaultVisualEmbedderModel'] = self.default_visual_embedder_model.to_map()

        if self.default_visual_llm_model is not None:
            result['DefaultVisualLlmModel'] = self.default_visual_llm_model.to_map()

        result['EmbeddingModels'] = []
        if self.embedding_models is not None:
            for k1 in self.embedding_models:
                result['EmbeddingModels'].append(k1.to_map() if k1 else None)

        result['GraphLlmModels'] = []
        if self.graph_llm_models is not None:
            for k1 in self.graph_llm_models:
                result['GraphLlmModels'].append(k1.to_map() if k1 else None)

        result['LlmModels'] = []
        if self.llm_models is not None:
            for k1 in self.llm_models:
                result['LlmModels'].append(k1.to_map() if k1 else None)

        if self.memory_types is not None:
            result['MemoryTypes'] = self.memory_types

        if self.multimodal_supported is not None:
            result['MultimodalSupported'] = self.multimodal_supported

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RerankModels'] = []
        if self.rerank_models is not None:
            for k1 in self.rerank_models:
                result['RerankModels'].append(k1.to_map() if k1 else None)

        result['VLModels'] = []
        if self.vlmodels is not None:
            for k1 in self.vlmodels:
                result['VLModels'].append(k1.to_map() if k1 else None)

        result['VisualEmbedderModels'] = []
        if self.visual_embedder_models is not None:
            for k1 in self.visual_embedder_models:
                result['VisualEmbedderModels'].append(k1.to_map() if k1 else None)

        result['VisualLlmModels'] = []
        if self.visual_llm_models is not None:
            for k1 in self.visual_llm_models:
                result['VisualLlmModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_models = []
        if m.get('AsrModels') is not None:
            for k1 in m.get('AsrModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyAsrModels()
                self.asr_models.append(temp_model.from_map(k1))

        if m.get('DefaultEmbeddingModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultEmbeddingModel()
            self.default_embedding_model = temp_model.from_map(m.get('DefaultEmbeddingModel'))

        if m.get('DefaultGraphLLMModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultGraphLLMModel()
            self.default_graph_llmmodel = temp_model.from_map(m.get('DefaultGraphLLMModel'))

        if m.get('DefaultLLMModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultLLMModel()
            self.default_llmmodel = temp_model.from_map(m.get('DefaultLLMModel'))

        if m.get('DefaultMemoryType') is not None:
            self.default_memory_type = m.get('DefaultMemoryType')

        if m.get('DefaultRerankModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultRerankModel()
            self.default_rerank_model = temp_model.from_map(m.get('DefaultRerankModel'))

        if m.get('DefaultVLModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVLModel()
            self.default_vlmodel = temp_model.from_map(m.get('DefaultVLModel'))

        if m.get('DefaultVisualEmbedderModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVisualEmbedderModel()
            self.default_visual_embedder_model = temp_model.from_map(m.get('DefaultVisualEmbedderModel'))

        if m.get('DefaultVisualLlmModel') is not None:
            temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyDefaultVisualLlmModel()
            self.default_visual_llm_model = temp_model.from_map(m.get('DefaultVisualLlmModel'))

        self.embedding_models = []
        if m.get('EmbeddingModels') is not None:
            for k1 in m.get('EmbeddingModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyEmbeddingModels()
                self.embedding_models.append(temp_model.from_map(k1))

        self.graph_llm_models = []
        if m.get('GraphLlmModels') is not None:
            for k1 in m.get('GraphLlmModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyGraphLlmModels()
                self.graph_llm_models.append(temp_model.from_map(k1))

        self.llm_models = []
        if m.get('LlmModels') is not None:
            for k1 in m.get('LlmModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyLlmModels()
                self.llm_models.append(temp_model.from_map(k1))

        if m.get('MemoryTypes') is not None:
            self.memory_types = m.get('MemoryTypes')

        if m.get('MultimodalSupported') is not None:
            self.multimodal_supported = m.get('MultimodalSupported')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rerank_models = []
        if m.get('RerankModels') is not None:
            for k1 in m.get('RerankModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyRerankModels()
                self.rerank_models.append(temp_model.from_map(k1))

        self.vlmodels = []
        if m.get('VLModels') is not None:
            for k1 in m.get('VLModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyVLModels()
                self.vlmodels.append(temp_model.from_map(k1))

        self.visual_embedder_models = []
        if m.get('VisualEmbedderModels') is not None:
            for k1 in m.get('VisualEmbedderModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyVisualEmbedderModels()
                self.visual_embedder_models.append(temp_model.from_map(k1))

        self.visual_llm_models = []
        if m.get('VisualLlmModels') is not None:
            for k1 in m.get('VisualLlmModels'):
                temp_model = main_models.DescribeApplicationAvailableModelsResponseBodyVisualLlmModels()
                self.visual_llm_models.append(temp_model.from_map(k1))

        return self

class DescribeApplicationAvailableModelsResponseBodyVisualLlmModels(DaraModel):
    def __init__(
        self,
        name: str = None,
        supported_modalities: List[str] = None,
    ):
        # The model name.
        self.name = name
        # The supported modalities.
        self.supported_modalities = supported_modalities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.supported_modalities is not None:
            result['SupportedModalities'] = self.supported_modalities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SupportedModalities') is not None:
            self.supported_modalities = m.get('SupportedModalities')

        return self

class DescribeApplicationAvailableModelsResponseBodyVisualEmbedderModels(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        dimensions: List[int] = None,
        name: str = None,
    ):
        # The default dimension.
        self.dimension = dimension
        # The available dimensions.
        self.dimensions = dimensions
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyVLModels(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyRerankModels(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyLlmModels(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyGraphLlmModels(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyEmbeddingModels(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        dimensions: List[int] = None,
        name: str = None,
    ):
        # The default vector dimensions of the model.
        self.dimension = dimension
        # The list of vector dimensions supported by the model.
        self.dimensions = dimensions
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultVisualLlmModel(DaraModel):
    def __init__(
        self,
        name: str = None,
        supported_modalities: List[str] = None,
    ):
        # The model name.
        self.name = name
        # The supported modalities.
        self.supported_modalities = supported_modalities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.supported_modalities is not None:
            result['SupportedModalities'] = self.supported_modalities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SupportedModalities') is not None:
            self.supported_modalities = m.get('SupportedModalities')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultVisualEmbedderModel(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        dimensions: List[int] = None,
        name: str = None,
    ):
        # The default dimension.
        self.dimension = dimension
        # The available dimensions.
        self.dimensions = dimensions
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultVLModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultRerankModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultLLMModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultGraphLLMModel(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyDefaultEmbeddingModel(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        dimensions: List[int] = None,
        name: str = None,
    ):
        # The default vector dimensions of the model.
        self.dimension = dimension
        # The list of vector dimensions supported by the model.
        self.dimensions = dimensions
        # The model name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationAvailableModelsResponseBodyAsrModels(DaraModel):
    def __init__(
        self,
        name: str = None,
        protocol: str = None,
    ):
        # The model name.
        self.name = name
        # The protocol used by the speech recognition model.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

