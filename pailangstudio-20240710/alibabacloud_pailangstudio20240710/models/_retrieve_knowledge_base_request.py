# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        hybrid_strategy_config: str = None,
        meta_data_filter_conditions: str = None,
        query: str = None,
        query_mode: str = None,
        rerank_config: str = None,
        rewrite_config: str = None,
        score_threshold: float = None,
        top_k: int = None,
        version_name: str = None,
        workspace_id: str = None,
    ):
        # 混合检索策略配置，选填。JSON格式字符串，JSON字段定义如下：
        # 
        # - Strategy：混合检索策略。取值为rrf（RRF融合）和weighted（加权融合）
        # 
        # - RRFK：RRF融合平滑参数，取值范围 [1, 100]
        # 
        # - Weight：weighted策略的权重，该值表示向量语义检索对最终得分的贡献比例。取值范围 [0, 1.0]
        self.hybrid_strategy_config = hybrid_strategy_config
        # 选填。元数据过滤检索条件。格式为JSON格式字符串，JSON字段定义如下：
        # 
        # - FilterCondition: 逻辑关系，取值：and、or。
        # - MetaDataFilters：过滤条件。多个条件之间按FilterCondition的逻辑关系处理。其中Key表示元数据Key；Value表示元数据值；Operator表示运算符，取值：==、!=、contains，contains仅支持file_name字段。
        self.meta_data_filter_conditions = meta_data_filter_conditions
        # 检索内容。
        # 
        # This parameter is required.
        self.query = query
        # 检索模式。
        # 
        # - dense: 语义检索。
        # - hybrid: 混合检索。
        self.query_mode = query_mode
        # Rerank配置，选填。JSON格式字符串，JSON字段定义如下：
        # 
        # - ConnectionId：模型服务连接ID
        # 
        # - Model：模型名称。若为百炼类型连接，支持的模型为 gte-rerank-v2
        # 
        # - TopK：返回排名最高的结果数
        self.rerank_config = rerank_config
        # Rewrite配置，选填。JSON格式字符串，JSON字段定义如下：
        # 
        # - ConnectionId：模型服务连接ID
        # 
        # - Model：模型名称。百炼连接支持的模型为qwen3-max、qwen-plus、qwen-flash
        # 
        # - Temprature：用于控制大模型生成内容的随机性，值越高结果越随机。取值范围 [0, 2.0]。
        # 
        # - TopP：生成过程中的核采样方法概率阈值，取值范围 [0, 1.0]
        # 
        # - PresensePenalty：存在惩罚，取值范围 [-2.0, 2.0]
        # 
        # - FrequencyPenalty：频率惩罚，取值范围 [-2.0~2.0]
        # 
        # - Seed：随机数种子，取值范围 [0, 2147483647]
        # 
        # - MaxTokens：控制模型生成结果的长度
        # 
        # - Stop：停止序列列表。遇到列表中的任何一个序列，模型停止输出。最多支持4个序列。
        # 
        # - EnableThingking：是否启用推理
        self.rewrite_config = rewrite_config
        # 相似度分数阈值。浮点型，取值范围[0, 1]。
        self.score_threshold = score_threshold
        # 返回排名最高的结果数。
        self.top_k = top_k
        # 知识库版本。默认v1。
        self.version_name = version_name
        # 知识库所在工作空间ID。
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hybrid_strategy_config is not None:
            result['HybridStrategyConfig'] = self.hybrid_strategy_config

        if self.meta_data_filter_conditions is not None:
            result['MetaDataFilterConditions'] = self.meta_data_filter_conditions

        if self.query is not None:
            result['Query'] = self.query

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.rerank_config is not None:
            result['RerankConfig'] = self.rerank_config

        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HybridStrategyConfig') is not None:
            self.hybrid_strategy_config = m.get('HybridStrategyConfig')

        if m.get('MetaDataFilterConditions') is not None:
            self.meta_data_filter_conditions = m.get('MetaDataFilterConditions')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('RerankConfig') is not None:
            self.rerank_config = m.get('RerankConfig')

        if m.get('RewriteConfig') is not None:
            self.rewrite_config = m.get('RewriteConfig')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

