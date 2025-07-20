




## Expected client output:
```json
{'messages': [HumanMessage(content="what's (3 + 5) x 12?", additional_kwargs={}, response_metadata={}, id='e330b525-5d66-47b7-a14e-8b4b4f4387c9'),
AIMessage(content="I'll calculate (3 + 5) x 12 for you by breaking it down into steps.\n\nFirst, I need to calculate the sum inside the parentheses (3 + 5):", additional_kwargs={'usage': {'prompt_tokens': 458, 'completion_tokens': 113, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 571
            }, 'stop_reason': 'tool_use', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, response_metadata={'usage': {'prompt_tokens': 458, 'completion_tokens': 113, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 571
            }, 'stop_reason': 'tool_use', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, id='run--d463a117-cf05-4d09-ab18-c7b580086720-0', tool_calls=[
            {'name': 'add', 'args': {'a': 3, 'b': 5
                }, 'id': 'toolu_bdrk_01CdtJ3LXr2SGZdvHN3oEwRW', 'type': 'tool_call'
            }
        ], usage_metadata={'input_tokens': 458, 'output_tokens': 113, 'total_tokens': 571, 'input_token_details': {'cache_creation': 0, 'cache_read': 0
            }
        }),
ToolMessage(content='8', name='add', id='0a748f69-be62-421d-a87b-3fb4c8925750', tool_call_id='toolu_bdrk_01CdtJ3LXr2SGZdvHN3oEwRW'),
AIMessage(content="Now that I have the result of (3 + 5) = 8, I'll multiply this by 12:", additional_kwargs={'usage': {'prompt_tokens': 583, 'completion_tokens': 96, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 679
            }, 'stop_reason': 'tool_use', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, response_metadata={'usage': {'prompt_tokens': 583, 'completion_tokens': 96, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 679
            }, 'stop_reason': 'tool_use', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, id='run--ea754713-6804-40e4-a6cf-63a015eeb2ae-0', tool_calls=[
            {'name': 'multiply', 'args': {'a': 8, 'b': 12
                }, 'id': 'toolu_bdrk_01ACeNzP6ka5obEGPJgRKVuM', 'type': 'tool_call'
            }
        ], usage_metadata={'input_tokens': 583, 'output_tokens': 96, 'total_tokens': 679, 'input_token_details': {'cache_creation': 0, 'cache_read': 0
            }
        }),
ToolMessage(content='96', name='multiply', id='44b39eda-bea5-40a1-a789-8ad6251454db', tool_call_id='toolu_bdrk_01ACeNzP6ka5obEGPJgRKVuM'),
AIMessage(content='The answer to (3 + 5) x 12 is 96.', additional_kwargs={'usage': {'prompt_tokens': 691, 'completion_tokens': 22, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 713
            }, 'stop_reason': 'end_turn', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, response_metadata={'usage': {'prompt_tokens': 691, 'completion_tokens': 22, 'cache_read_input_tokens': 0, 'cache_write_input_tokens': 0, 'total_tokens': 713
            }, 'stop_reason': 'end_turn', 'thinking': {}, 'model_id': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0', 'model_name': 'us.anthropic.claude-3-7-sonnet-20250219-v1: 0'
        }, id='run--ffd8572a-1117-4f3a-9f0d-13b7446b1bf7-0', usage_metadata={'input_tokens': 691, 'output_tokens': 22, 'total_tokens': 713, 'input_token_details': {'cache_creation': 0, 'cache_read': 0
            }
        })
    ]
}
```