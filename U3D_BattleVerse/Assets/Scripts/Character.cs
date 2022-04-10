using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Character : ICharacter
{
    protected string firstName;
    protected string lastName;
    protected string[] aliases;

    public string FirstName { get { return firstName; } set { } }
    public string LastName { get { return lastName; } set { } }
    public string MainAlias { get { return aliases[0]; } set { } }

    public string FullName {
        get { return string.Format("{0} {1}", firstName, lastName); }
        set { }
    }

    public string[] AliasList { get { return aliases; } set { } }
}
