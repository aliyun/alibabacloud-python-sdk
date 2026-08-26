# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeSpaceRequest(DaraModel):
    def __init__(
        self,
        dbtype: str = None,
        description: str = None,
        embedding_dimension: int = None,
        embedding_model: str = None,
        enforce_acl: bool = None,
        llmmodel: str = None,
        name: str = None,
        ossaccess_key: str = None,
        ossbucket: str = None,
        osssecret_key: str = None,
        region_id: str = None,
        rerank_model: str = None,
        security_group_id: str = None,
        sharding_size: int = None,
        sharding_strategy: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The database engine type.
        self.dbtype = dbtype
        # The description of the knowledge space. The description can be up to 512 characters in length.
        self.description = description
        # The vector dimensions.
        # 
        # This parameter is required.
        self.embedding_dimension = embedding_dimension
        # The name of the embedding model.
        # 
        # This parameter is required.
        self.embedding_model = embedding_model
        # Specifies whether to enable ACL-based authentication for the knowledge space.
        self.enforce_acl = enforce_acl
        # The name of the large language model.
        self.llmmodel = llmmodel
        # The name of the knowledge space. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # OSS AK
        # 
        # This parameter is required.
        self.ossaccess_key = ossaccess_key
        # The name of an existing OSS bucket in the same region.
        # 
        # This parameter is required.
        self.ossbucket = ossbucket
        # OSS SK
        # 
        # This parameter is required.
        self.osssecret_key = osssecret_key
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the reranking model.
        self.rerank_model = rerank_model
        # The security group ID.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The shard size, in tokens.
        # 
        # This parameter is required.
        self.sharding_size = sharding_size
        # The sharding strategy. Valid values:
        # 
        # - hierarchical (default)
        # - hybrid
        # 
        # This parameter is required.
        self.sharding_strategy = sharding_strategy
        # The vSwitch for automatic creation of the database.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The VPC for automatic creation of the database.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The active zone for automatic creation of the database.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.enforce_acl is not None:
            result['EnforceAcl'] = self.enforce_acl

        if self.llmmodel is not None:
            result['LLMModel'] = self.llmmodel

        if self.name is not None:
            result['Name'] = self.name

        if self.ossaccess_key is not None:
            result['OSSAccessKey'] = self.ossaccess_key

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.osssecret_key is not None:
            result['OSSSecretKey'] = self.osssecret_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.sharding_size is not None:
            result['ShardingSize'] = self.sharding_size

        if self.sharding_strategy is not None:
            result['ShardingStrategy'] = self.sharding_strategy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('EnforceAcl') is not None:
            self.enforce_acl = m.get('EnforceAcl')

        if m.get('LLMModel') is not None:
            self.llmmodel = m.get('LLMModel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OSSAccessKey') is not None:
            self.ossaccess_key = m.get('OSSAccessKey')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSSecretKey') is not None:
            self.osssecret_key = m.get('OSSSecretKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankModel') is not None:
            self.rerank_model = m.get('RerankModel')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ShardingSize') is not None:
            self.sharding_size = m.get('ShardingSize')

        if m.get('ShardingStrategy') is not None:
            self.sharding_strategy = m.get('ShardingStrategy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

