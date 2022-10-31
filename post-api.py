
import requests

# Contants

CONTENT_TYPE ='application/json'

# headers = {
#   'Content-Type': CONTENT_TYPE,
#   'x-auth-token': '\'token\''
# }

# Body
values = '''{
  "gap_name": "Alleluia Testing GAP 6",
  "gap_weight": 20,
  "gap_score": 100,
  "picture_text": "Describe how pictures will be taken",
  "sections": [
    {
      "section_name": "Q 2.8.1. LOOK: At the colour of the coffee tree leaves. Are the leaves dark green or are some leaves yellow, pale green, or brown?",
      "questions": [
        {
          "question": "Nearly all leaves are dark green and less than 5% (less than 5 in 100) are yellow, pale green, or brown.",
          "description": "de",
          "question_type": "yes_no",
          "weight": 10,
          "answers": [],
          "is_not_applicable": false
        }
      ]
    },
    {
      "section_name": " LOOK: Which pruning method(s) have been used on the majority of trees?",
      "questions": [
        {
          "question": "Quality of tools&materials used in pruning ",
          "description": "de",
          "question_type": "multiple_single",
          "weight": 20,
          "answers": [
            {
              "answer": "If Conventional tools: Pruning shear/secateur&Saw",
              "description": "de",
              "weight": 15,
              "is_not_applicable": false
            },
            {
              "answer": " If Non conventional tools ",
              "description": "de",
              "weight": 5,
              "is_not_applicable": false
            },
            {
              "answer": "Cleaning of pruning tools to avoid the spread of diseases between trees",
              "description": "de",
              "weight": 5,
              "is_not_applicable": false
            }
          ],
          "is_not_applicable": false
        }
      ]
    },
    {
      "section_name": "This is a section name",
      "questions": [
        {
          "question": "This is the question to be asked",
          "description": "Marks Input",
          "question_type": "mark_input",
          "weight": 20,
          "answers": [],
          "is_not_applicable": false
        }
      ]
    },
    {
      "section_name": "This is a section name",
      "questions": [
        {
          "question": "This is the question to be asked",
          "description": "Marks Input",
          "question_type": "multiple_apply",
          "weight": 20,
          "answers": [
            {
              "answer": "This is an answer",
              "description": "Answer Description",
              "weight": 5,
              "is_not_applicable": false
            },
            {
              "answer": "This is an answer",
              "description": "Answer Description",
              "weight": 5,
              "is_not_applicable": false
            },
            {
              "answer": "This is an answer",
              "description": "Answer Description",
              "weight": 5,
              "is_not_applicable": false
            },
            {
              "answer": "This is an answer",
              "description": "Answer Description",
              "weight": 0,
              "is_not_applicable": false
            }
          ],
          "is_not_applicable": false
        }
      ]
    }
  ]
}'''

response = requests.post('https://staging.smartkungahara.rw/core/api/v1.1/gaps', data=values, headers=headers)

print(response.status_code)
print(response.headers)
print(response.json())