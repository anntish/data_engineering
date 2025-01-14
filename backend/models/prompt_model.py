from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class PromptResponse(Base):
    __tablename__ = 'benchmark_llm_monitoring'

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    prompt_label = Column(String, nullable=True)  
    response_refusal_label = Column(String, nullable=True)  
    response_label = Column(String, nullable=True)  
    model = Column(String, nullable=False)
    language = Column(String, nullable=True) 
    source = Column(String, nullable=True) 
    prompt_length = Column(Integer, nullable=True) 
    response_length = Column(Integer, nullable=True)  
    security_rag_prompt_harm_label = Column(String, nullable=True) 
    security_rag_response_refusal_label = Column(String, nullable=True) 
    security_rag_response_harm_label = Column(String, nullable=True) 
    sec_rag_prompt_label = Column(String, nullable=True)  
    
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
